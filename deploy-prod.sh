#!/bin/bash

set -e
docker build -t realm-dj-base-image:latest -f ./Dockerfiles/base.Dockerfile .
docker build -t eu.gcr.io/realm-rn-dj/api-prod:latest -f ./Dockerfiles/prod.Dockerfile .
docker push eu.gcr.io/realm-rn-dj/api-prod:latest
gcloud config set run/region europe-west1
gcloud config set project realm-rn-dj
gcloud run deploy realm-dj --image eu.gcr.io/realm-rn-dj/api-prod:latest --platform managed --port 8080