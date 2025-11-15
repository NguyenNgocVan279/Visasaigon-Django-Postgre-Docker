#!/bin/sh
set -e

echo "Waiting for PostgreSQL to be ready..."
while ! nc -z db 5432; do
  sleep 1
done

echo "Database is ready!"

echo "Running migrations..."
python manage.py migrate --noinput

# echo "Collecting static files..."
# python manage.py collectstatic --noinput

echo "Starting Gunicorn server..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
