#!/bin/sh

echo "Waiting for Database..."

while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
  sleep 0.1
done
#
python manage.py migrate

DJANGO_SUPERUSER_PASSWORD= \
DJANGO_SUPERUSER_USERNAME=test@mail.com \
DJANGO_SUPERUSER_EMAIL=test@mail.com \
DJANGO_SUPERUSER_LAST_NAME=Test \
DJANGO_SUPERUSER_FIRST_NAME=User \
python manage.py createsuperuser --no-input || true

exec "$@"