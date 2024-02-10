#!/usr/bin/env bash

python manage.py collectstatic --noinput &
python manage.py compilemessages &
python manage.py migrate &
exec "$@"
