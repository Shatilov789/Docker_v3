#! /bin/bash

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:8000
gunicorn ljingo.wsgi -c ./gunicorn/gunicorn.py -b 0.0.0.0:8000