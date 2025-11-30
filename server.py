import os
import http.server
import socketserver

from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    def get_game_list(self)
        msg = f"games list: none yet"
        self.wfile.write(msg.encode())

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello! you requested %s' % (self.path)
        self.wfile.write(msg.encode())
        if self.path == "/game_list":
            self.get_game_list()


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
