# Use official Python image
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy entire project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start Django via gunicorn
CMD ["gunicorn", "career_cast.wsgi:application", "--bind", "0.0.0.0:8000"]
