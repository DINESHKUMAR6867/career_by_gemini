# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for Pillow, PyPDF2, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files (if using Django static)
RUN python manage.py collectstatic --noinput

# Expose port (Vercel sets PORT)
ENV PORT 8000
ENV PYTHONUNBUFFERED=1

# Run server on 0.0.0.0
CMD ["gunicorn", "career_cast.wsgi:application", "--bind", "0.0.0.0:8000"]
