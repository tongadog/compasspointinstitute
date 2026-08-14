import os
import http.server
import socketserver

os.chdir("/Users/caiwd/Documents/cpi-website")
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8934), Handler) as httpd:
    httpd.serve_forever()
