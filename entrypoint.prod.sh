#!/bin/sh

if [ "$DATABASE" = "realm_django" ]
then
    echo "Waiting for realm_django..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "realm_django started"
fi

exec "$@"