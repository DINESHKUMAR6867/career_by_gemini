# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Enable buffering
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Install system dependencies for PDFs and images
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    libmagic-dev \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run Django with Gunicorn
CMD ["gunicorn", "career_cast.wsgi:application", "--bind", "0.0.0.0:8000"]
