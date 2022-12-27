#!/bin/bash

./cloud_sql_proxy -instances=realm-rn-dj:europe-west1:realm-django=tcp:8000 -credential_file=secrets/db-proxy.json &

# wait for proxy to spin up
sleep 1

# Start the server 
/usr/local/bin/gunicorn base.wsgi:application -w 2 -b :8080

# Testing with service account cloudrun