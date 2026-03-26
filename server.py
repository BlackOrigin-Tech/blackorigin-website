#!/usr/bin/env python3
import http.server
import socketserver

PORT = 5000

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        print(format % args, flush=True)

with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving on port {PORT}", flush=True)
    httpd.serve_forever()
