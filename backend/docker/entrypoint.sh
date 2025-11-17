#!/bin/sh
set -e

echo "Waiting for PostgreSQL to be ready..."
while ! nc -z db 5432; do
  sleep 1
done

echo "Database is ready!"

# Tạo migration nếu chưa có
echo "Running makemigrations..."
python manage.py makemigrations

# Migrate database
echo "Running migrations..."
python manage.py migrate --noinput

# Dev: chạy server Django với DEBUG=True
if [ "$DJANGO_ENV" = "dev" ]; then
  echo "Starting Django development server..."
  python manage.py runserver 0.0.0.0:8000
else
  # Prod: collect static và chạy Gunicorn
  echo "Collecting static files..."
  python manage.py collectstatic --noinput
  echo "Starting Gunicorn server..."
  gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
fi
