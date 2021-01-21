#!/bin/bash
echo 'debut'
python manage.py clearsessions
echo 'fin'
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
