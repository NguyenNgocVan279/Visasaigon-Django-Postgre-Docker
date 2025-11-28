#!/bin/sh
set -e

echo "📌 Checking PostgreSQL availability..."
until nc -z "${POSTGRES_HOST:-db}" "${POSTGRES_PORT:-5432}"; do
  echo "⏳ Waiting for PostgreSQL..."
  sleep 2
done

echo "🚀 Applying migrations..."
python manage.py migrate --noinput

# Collectstatic chỉ chạy ở môi trường prod
if [ "$DJANGO_ENV" = "prod" ]; then
  echo "📁 Collecting static files..."
  python manage.py collectstatic --noinput

  # Tạo superuser nếu cần
  if [ "$CREATE_SUPERUSER" = "true" ]; then
    echo "👤 Creating superuser if not exists..."
    python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
username = '$DJANGO_SUPERUSER_USERNAME'
email = '$DJANGO_SUPERUSER_EMAIL'
password = '$DJANGO_SUPERUSER_PASSWORD'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created:', username)
else:
    print('Superuser already exists:', username)
"
  fi

  echo "🔥 Starting Gunicorn..."
  exec gunicorn config.wsgi:application -c /app/docker/gunicorn.conf.py

else
  echo "🔧 Starting Django development server..."
  exec python manage.py runserver 0.0.0.0:8000
fi
