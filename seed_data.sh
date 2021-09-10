#!/bin/bash

rm -rf dubsapi/migrations
rm db.sqlite3
python manage.py makemigrations dubsapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata customers
python manage.py loaddata product_types
python manage.py loaddata products
python manage.py loaddata topping_types
python manage.py loaddata toppings
python manage.py loaddata payments
python manage.py loaddata orders
python manage.py loaddata lineitems
python manage.py loaddata lineitemtoppings
