# Dockerfile
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port for Vercel
EXPOSE 8000

# Start the app
CMD ["gunicorn", "career_cast.wsgi:application", "--bind", "0.0.0.0:8000"]
