#!/bin/bash

rm -rf dubsapi/migrations
rm db.sqlite3
python manage.py makemigrations dubsapi
python manage.py migrate
# heroku run python manage.py loaddata users --app dubs-doubles
# heroku run python manage.py loaddata tokens --app dubs-doubles
heroku run python manage.py loaddata customers product_types products topping_types toppings payments orders lineitems lineitemtoppings --app dubs-doubles
# heroku run python manage.py loaddata product_types --app dubs-doubles
# heroku run python manage.py loaddata products --app dubs-doubles
# heroku run python manage.py loaddata topping_types --app dubs-doubles
# heroku run python manage.py loaddata toppings --app dubs-doubles
# heroku run python manage.py loaddata payments --app dubs-doubles
# heroku run python manage.py loaddata orders --app dubs-doubles
# heroku run python manage.py loaddata lineitems --app dubs-doubles
# heroku run python manage.py loaddata lineitemtoppings --app dubs-doubles
