#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import unquote

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the path
        path = unquote(self.path.split('?')[0])

        # Remove trailing slash
        if path.endswith('/') and path != '/':
            path = path[:-1]

        # If path has no extension and file doesn't exist, try adding .html
        if '.' not in os.path.basename(path):
            if path == '/' or path == '':
                self.path = '/index.html'
            else:
                # Check if .html version exists
                html_file = path[1:] + '.html' if path.startswith('/') else path + '.html'
                if os.path.isfile(html_file):
                    self.path = path + '.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8000
Handler = CustomHandler

print(f"🚀 Starting server at http://localhost:{PORT}")
print(f"📁 Serving: {os.getcwd()}")
print("")
print("Press Ctrl+C to stop")
print("")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped")
