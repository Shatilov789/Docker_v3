#! /bin/bash

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000