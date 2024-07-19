#!/bin/bash

rm db.sqlite3
rm -rf ./tripapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations tripapi
python3 manage.py migrate tripapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata trip

