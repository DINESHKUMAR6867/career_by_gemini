import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_cast.settings')
django.setup()

from django.core.management import execute_from_command_line

# Delete and recreate migrations
print("Resetting migrations...")
execute_from_command_line(['manage.py', 'migrate', 'main_app', 'zero'])
execute_from_command_line(['manage.py', 'makemigrations', 'main_app'])
execute_from_command_line(['manage.py', 'migrate'])
print("Migrations reset complete!")
