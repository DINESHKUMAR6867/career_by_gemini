import os
import sys
from http.server import BaseHTTPRequestHandler


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_cast.settings')

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            import django
            django.setup()
            
            from django.core.management import execute_from_command_line
            
            # Run migrations
            execute_from_command_line(['manage.py', 'migrate'])
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Migrations completed successfully!')
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Migration failed: {str(e)}'.encode())

def app(environ, start_response):
    handler = Handler(environ, start_response)
    return handler
