#!/bin/sh
# set -e

# Wait for the database to be ready before migrating
if [ ! -z "$DB_HOST" ]; then
  >&2 echo "Waiting for database connection on $DB_HOST:$DB_PORT"
  until nc -z $DB_HOST $DB_PORT
  do
    >&2 echo "Waiting for database connection..."
    sleep 1
  done
  >&2 echo "Waiting for database connection... Done"
fi

if [ $DJANGO_MANAGE_MIGRATE = 'on' ]; then
  python manage.py collectstatic --noinput
  python manage.py migrate --noinput
  python manage.py createcachetable
  python manage.py createsuperuser --noinput
fi

exec "$@"
