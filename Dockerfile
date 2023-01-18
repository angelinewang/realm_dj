FROM python:3.10

RUN apt-get install bash
RUN mkdir /usr/src/app
COPY . /usr/src/app

# COPY pyproject.toml /usr/src/app/
WORKDIR /usr/src/app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

# RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O /usr/src/app/cloud_sql_proxy

# RUN chmod +x /usr/src/app/cloud_sql_proxy

# RUN ln -sf /dev/stdout /var/log/access.log && \
#     ln -sf /dev/stderr /var/log/error.log

# RUN ./cloud_sql_proxy -instances="realm-rn-dj:europe-west1:realm-django"=tcp:8000 -credential_file=secrets/db-proxy.json &

ADD . /usr/src/app
CMD gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 base.wsgi:application

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.

