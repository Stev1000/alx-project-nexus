# Use Python 3.12 slim as base
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (needed for psycopg2 and compilation)
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (layer caching optimization)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run collectstatic and migrate, then start Gunicorn
#CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate --noinput && python manage.py createsu && gunicorn ecommerce_backend.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 2"]
# Run collectstatic, migrate, createsu, load fixtures, then start Gunicorn
CMD ["sh", "-c", "python manage.py collectstatic --noinput && \
                  python manage.py migrate --noinput && \
                  python manage.py createsu && \
                  (python manage.py loaddata seed_data.json || true) && \
                  gunicorn ecommerce_backend.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 2"]
