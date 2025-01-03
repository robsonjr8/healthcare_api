#!/usr/bin/bash

/usr/src/.venv/bin/python manage.py makemigrations
/usr/src/.venv/bin/python manage.py migrate --noinput
/usr/src/.venv/bin/python manage.py collectstatic --noinput --clear
/usr/src/.venv/bin/gunicorn healthcare.wsgi --bind $1:$2
