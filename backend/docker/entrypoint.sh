#!/bin/sh
set -e

echo "==== Checking database connection ===="
until nc -z "${POSTGRES_HOST:-db}" "${POSTGRES_PORT:-5432}"; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

echo "Applying migrations..."
python manage.py migrate --noinput

if [ "$DJANGO_ENV" = "prod" ]; then
  echo "Collecting static files..."
  python manage.py collectstatic --noinput

  if [ "$CREATE_SUPERUSER" = "true" ]; then
    echo "Creating superuser..."
    python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser(
        '$DJANGO_SUPERUSER_USERNAME',
        '$DJANGO_SUPERUSER_EMAIL',
        '$DJANGO_SUPERUSER_PASSWORD'
    )
EOF
  fi

  echo "Starting Gunicorn..."
  exec gunicorn config.wsgi:application -c /app/docker/gunicorn.conf.py
else
  echo "Starting Django development server..."
  python manage.py runserver 0.0.0.0:8000
fi
