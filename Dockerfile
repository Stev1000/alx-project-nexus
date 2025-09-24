# Use Python 3.12 slim as base
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (needed for psycopg2)
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

RUN python manage.py collectstatic --noinput

# Run with Gunicorn in production
CMD ["gunicorn", "ecommerce_backend.wsgi:application", "--bind", "0.0.0.0:8000"]

