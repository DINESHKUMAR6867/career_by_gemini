import os
import sys
from http.server import BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {'status': 'migration_endpoint_ready'}
        self.wfile.write(json.dumps(response).encode())

def app(environ, start_response):
    handler = Handler(environ, start_response)
    return handler
