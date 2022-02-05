#!/bin/sh

echo "Waiting for Database..."

while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
  sleep 0.1
done
#
python manage.py migrate
exec "$@"