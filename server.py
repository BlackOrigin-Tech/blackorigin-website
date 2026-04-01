#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 5000

class BlackOriginHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            try:
                with open('404.html', 'rb') as f:
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.wfile.write(b'<h1>404 Not Found</h1>')
            return
        super().send_error(code, message, explain)

    def log_message(self, format, *args):
        print(format % args, flush=True)

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), BlackOriginHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}", flush=True)
    httpd.serve_forever()
