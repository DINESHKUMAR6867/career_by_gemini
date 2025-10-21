from http.server import BaseHTTPRequestHandler
import os
import sys

# Add project to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_cast.settings')

import django
django.setup()

from django.core.management import execute_from_command_line

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        try:
            execute_from_command_line(['manage.py', 'migrate', '--noinput'])
            self.wfile.write(b'Migrations completed successfully!')
        except Exception as e:
            self.wfile.write(f'Error: {str(e)}'.encode())

# For Vercel
def app(environ, start_response):
    handler = Handler(environ, start_response)
    return handler
