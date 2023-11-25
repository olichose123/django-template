#!/bin/sh

if [ $DJANGO_MANAGE_MIGRATE = 'on' ]; then
  python manage.py collectstatic --noinput
  python manage.py migrate --noinput
  python manage.py createcachetable
  python manage.py createsuperuser --noinput
fi

exec "$@"
