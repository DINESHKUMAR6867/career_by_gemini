# import os
# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "career_cast.settings")

# # Vercel expects this name
# app = get_wsgi_application()

# try:
#     from django.core.management import call_command
#     call_command("migrate", interactive=False, verbosity=0)
# except Exception as e:
#     print("Migrations skipped:", e)
import os
import sys
from django.core.wsgi import get_wsgi_application

# Add project directory to Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_cast.settings')

# Force run migrations on every cold start
try:
    import django
    django.setup()
    
    from django.db import connection
    from django.core.management import execute_from_command_line
    
    # Check if django_migrations table exists
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'django_migrations'
            );
        """)
        table_exists = cursor.fetchone()[0]
        
        if not table_exists:
            print("Running initial migrations...")
            execute_from_command_line(['manage.py', 'migrate', '--noinput'])
        else:
            print("Migrations table exists, skipping auto-migration")
            
except Exception as e:
    print(f"Migration check completed: {e}")

app = get_wsgi_application()

