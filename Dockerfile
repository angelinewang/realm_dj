FROM python:3.10
RUN mkdir /app 
COPY . /app
COPY pyproject.toml /app 
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main
CMD gunicorn -b :8080 main:app
# RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
# RUN chmod +x cloud_sql_proxy
# RUN ./cloud_sql_proxy -instances="realm-rn-dj:europe-west1:realm-django"=tcp:5432
# CMD [ "uwsgi", "--socket", "0.0.0.0:3031", \
#                "--uid", "uwsgi", \
#                "--plugins", "python3", \
#                "--protocol", "uwsgi", \
#                "--wsgi", "main:application" ]
# CMD [ "python", "./manage.py", "runserver", "0.0.0.0:5000", "--settings=django_settings" ]
# CMD exec gunicorn --bind :3307 --workers 1 --threads 8 --timeout 0 base:app
# CMD ["./cloud_sql_proxy", "-instances=realm-rn-dj:europe-west1:realm-django=tcp:0.0.0.0:8000", "-credential_file=/credentials.json"]
# ENTRYPOINT gunicorn -b :8080 base.wsgi:application --timeout 0
# CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "base.wsgi:application"]
# # SERVICE URL/admin WORKING
# But when attempt to log in, it does not work
# # Use the official lightweight Python image.
# # https://hub.docker.com/_/python
# FROM python:3.10-slim


# # Allow statements and log messages to immediately appear in the Knative logs
# ENV PYTHONUNBUFFERED True

# # Copy local code to the container image.
# ENV APP_HOME /app
# WORKDIR $APP_HOME
# COPY . ./

# # Install production dependencies.
# RUN pip install --no-cache-dir -r requirements.txt

# # Run the web service on container startup. Here we use the gunicorn
# # webserver, with one worker process and 8 threads.
# # For environments with multiple CPU cores, increase the number of workers
# # to be equal to the cores available.
# # Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
# CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app

