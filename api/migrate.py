import os
import sys
from http.server import BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Add project to Python path
            sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_cast.settings')
            
            import django
            django.setup()
            
            from django.core.management import execute_from_command_line
            
            # Run migrations
            execute_from_command_line(['manage.py', 'migrate', '--noinput'])
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'status': 'success', 'message': 'Migrations completed successfully!'}
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'status': 'error', 'message': f'Migration failed: {str(e)}'}
            self.wfile.write(json.dumps(response).encode())

def app(environ, start_response):
    handler = Handler(environ, start_response)
    return handler
