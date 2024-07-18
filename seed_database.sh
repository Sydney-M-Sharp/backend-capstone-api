#!/bin/bash

rm db.sqlite3
rm -rf ./trip-app-api/migrations
python3 manage.py migrate
python3 manage.py makemigrations trip-app-api
python3 manage.py migrate trip-app-api
python3 manage.py loaddata users
python3 manage.py loaddata tokens

