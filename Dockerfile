# ===============================
# Use Python 3.12 slim as base
# ===============================
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (needed for psycopg2 and compilation)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Install Python dependencies
# ===============================
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ===============================
# Copy project files
# ===============================
COPY . .

# ===============================
# Environment variables
# ===============================
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=ecommerce_backend.settings

# ===============================
# Collect static files at build time (safe for Render)
# ===============================
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# ===============================
# Start Gunicorn
# ===============================
CMD ["gunicorn", "ecommerce_backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=3", "--threads=2", "--timeout=120"]
