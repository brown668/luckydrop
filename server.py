import os
os.chdir('/Users/brown/Documents/Agent/minigame')
import http.server
import socketserver

PORT = 4321
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
