#!/usr/bin/env bash

python manage.py collectstatic --noinput &
python manage.py compilemessages &
python manage.py migrate &
python manage.py loaddata --format jsonl initial.jsonl &2 > /dev/null &
exec "$@"
