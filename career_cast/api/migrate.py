from http.server import BaseHTTPRequestHandler
import os
import sys

# Add Django project to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set Django settings
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
            # Run migrations
            execute_from_command_line(['manage.py', 'migrate'])
            self.wfile.write(b'Migrations completed successfully!')
        except Exception as e:
            self.wfile.write(f'Migration error: {str(e)}'.encode())

def main():
    # This is for local testing
    execute_from_command_line(['manage.py', 'migrate'])

if __name__ == '__main__':
    main()
