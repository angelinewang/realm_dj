#!/bin/bash

./cloud_sql_proxy -instances=realm-rn-dj:europe-west1:realm-django=tcp:8000 -credential_file=secrets/db-proxy.json &

# wait for proxy to spin up
sleep 1

# Start the server 
/usr/local/bin/gunicorn -w 2 -b :8080 base.wsgi:application

# After PORT, must run the "application" variable inside base.wsgi
# This is often remained main for App Engine

# Testing with service account cloudrun