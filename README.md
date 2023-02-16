Backend Tech Stack:
- Django Framework 
- ORM 
- PostgreSQL Relational Database

Backend Languages:
- Python 
- SQL

Data Structure Diagram:
[Link to Canva File](https://www.canva.com/design/DAFRuhtn9Pc/rZ5cUC7uPvzlXqN5w0VbeQ/view?utm_content=DAFRuhtn9Pc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
Future Database ER Diagram:
[Link to Lucid App File](https://lucid.app/lucidchart/72e0d6f7-f28b-4d48-b3b6-4a4d29c5fadb/edit?viewport_loc=-289%2C-192%2C1540%2C1473%2C0_0&invitationId=inv_d0ac2e0d-b1e8-4eb4-871b-9e6fb19f9631)

Views:
- Generics

### Flow of Invite Creation:
1. Frontend: Determine if User is Host 
2. Frontend: Get Party associated with User --> With authUserId in URL Parameters
3. Backend: Call CreateInvite API with Guest Id & Party Id as fields in body of the anonymous call

Since Party automatically associated with Host Id, no need to pass Id of authenticated User when making POST Request

### Testing Data
#### Testing Hosts
IDs: 12, 13, 14, 15, 16
Names: Host 1, Host 2, Host 3, Host 4, Host 5

IDs for Parties: 37, 38, 39, 40, 41
Flats: PASTPARTY1, PASTPARTY2, FUTUREPARTY1, FUTUREPARTY2, FUTUREPARTY3

### Parties Screens 
Validation that parties shown on both Invited and Confirmed screens
= Only include parties whose last entry (12 hours after first entry) is in the future

### SignUp Form 
Unable to use FileUploadParser because not using a native client
--> Only able to use MultiPartParser
[Django REST Framework Parsers](https://www.django-rest-framework.org/api-guide/parsers/)

### Photo Upload 
1. Base64 Encoded in frontend
2. Saved as Base64 in backend

### Google Cloud Configuration Terminal Commands 
1. gcloud auth login 
2. gcloud app create --region=europe-west

### Google Cloud SQL Instance
Database Name: realm-django
Username: postgres
Password: kittyKat7765

### Cloud Storage Bucket 
Purpose 
- Storing Django's included static assets, user-uploaded media
- Stored in highly-available object storage using Cloud Storage

Usage
[django-storages package handling Django interaction with storage backend](https://django-storages.readthedocs.io/en/latest/)

### Daily Notes 
#### Wednesday 14th December 2022
##### Tasks Completed:
1. Change all passwords - DONE 
- All Social Accounts the same: rosePetals9910
--> angeline@realmsocialapp.com
--> angeline@realmpartyapp.com

- Technology stuff for Realm: all different
--> realm_django postgres database user "postgres": blueLilacs8830
--> realm_django Google Cloud SQL Instance database username "postgres": blueLilacs8830
--> Master Password for postgreSQL Server: angeline

2. Record all passwords - DONE 

3. Finish Django Google Cloud tutorial

#### Run app on local computer 
Start Cloud SQL Auth proxy 
--> Terminal Command Suggested: `./cloud_sql_proxy -instances="realm-rn-dj:europe-west1:realm-django"=tcp:5432`
--> However, this threw an error: `listen tcp 127.0.0.1:5432: bind: An attempt was made to access a socket in a way forbidden by its access permissions`
--> So, changes the tcp to `8000`
--> SOLUTION: cloud sql proxy must be run on different port to the database instance 
--> Terminal Command that worked in the end to start the Cloud SQL Auth proxy: `./cloud_sql_proxy -instances="realm-rn-dj:europe-west1:realm-django"=tcp:8000`

#### PORTs
python manage.py runserver 
cloud sql auth proxy 
& sql instance database 
--> All 3 need to be run on different PORTs

Database: `5432`
Cloud SQL Auth Proxy: `8000`
Run Server: 8080 `python manage.py runserver 8080`
--> For fullstack app to connect to app engine database instance: It is not needed to use terminal command `python manage.py 8080`
--> When app is opened, it will automatically connect through PORT 5432 (which is proxied through 8000)


#### app.yaml File for Python runtime
[The Python runtime](https://cloud.google.com/appengine/docs/flexible/python/runtime)
[Google Cloud app.yaml Configuration file Documentation](https://cloud.google.com/appengine/docs/flexible/reference/app-yaml?tab=python#general)
--> Resource above may be needed again when creating a Service 
Specifying `runtime: custom` allows runtime configuration through `Dockerfile`

#### Dockerfile Configuration 
python version specified in Dockerfile be the same as python version used by poetry in pyproject.toml 
[Dockerizing Python Poetry Applications](https://medium.com/@harpalsahota/dockerizing-python-poetry-applications-1aa3acb76287)
[Packaging python using Poetry on Google Cloud](https://dev.to/sivakon/packaging-python-using-poetry-on-google-cloud-l8ds)

#### Download Cloud SQL Auth proxy 
Ended up saving [this file](https://dl.google.com/cloudsql/cloud_sql_proxy_x64.exe) as cloud_sql_proxy.exe and placing it in the root of the realm_dj directory
--> Consulted [this webpage](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy)

### Backend Package Management
Packages are managed with `poetry`
--> App Engine installs all dependencies from poetry.lock file 

### Create requirements.txt file
= Which includes packages installed through poetry 
`poetry export --without-hashes --format=requirements.txt > requirements.txt`
--> Terminal Command
--> App Engine needs the file to be exported without hashes
--> Original Reference: [Poetry - generate requirements.txt](https://testdriven.io/tips/eb1fb0f9-3547-4ca2-b2a8-1c037ba856d8/)
--> Another more detailed reference: [Reducing requirements.txt - Substack - With extended section on Poetry](https://stackoverflow.com/questions/63655310/reducing-requirements-txt)
--> I don't think a `requirements.txt` file is necessary if I have a `poetry.lock` file 


### Connect Google Cloud SQL Instance to PGAdmin
[Connecting to GCP’s Cloud SQL (PostgresSQL) from PgAdmin — 3 simple steps](https://cshiva.medium.com/connecting-to-gcps-cloud-sql-postgressql-from-pgadmin-3-simple-steps-2f4530488a4c)

1. Export data from regular PostgreSQL Database realm_django
--> using pg_dump
2. Import data into Cloud SQL 
--> using pg_restore

### Database Secrets
#### Storage Location
Under "django-settings"
--> Variables set in this secret:
1. DATABASE_URL 
2. GS_BUCKET_NAME 
3. SECRET_KEY
[Here is the link to secrets](https://console.cloud.google.com/security/secret-manager/secret/django_settings/versions?authuser=0&project=realm-rn-dj)

#### View Database Secrets 
1. Go to Secret Manager
2. Find "django-settings"
3. Click on 3 dots under "Actions"
4. Click on "Secret Value"

#### Webpage w/ Instructions to Create & Delete env file
[Running Django on the App Engine flexible environment - Google Cloud](https://cloud.google.com/python/django/flexible-environment#linuxmacos_2)


#### Access to django-settings 
The secret is accessible by: realm-rn-dj@appspot.gserviceaccount.com through its Role: Secret Manager Secret Accessor


### Mon 19th Dec 2022
1. Updated the database password in Secret Manager "django-settings" and in .env file in realm_dj


### Backend Deployment Tech Stack 
Previously Decided to use:
Django on App Engine Flexible Environment
Instructions for deployment can be found [here](https://cloud.google.com/python/django/flexible-environment#linuxmacos_2)

Decided is better to use:
Cloud Run 
Arguments why it is better [Cloud Run vs App Engine: a head-to-head comparison using facts and science - Paul Craig](https://dev.to/pcraig3/cloud-run-vs-app-engine-a-head-to-head-comparison-using-facts-and-science-1225)
--> Cloud Run: 99% Cheaper because only charges you when there are API requests, and boots up the container then
--> Cloud Run = Containerized Serverless
--> Cloud Run = Charges you for the time spent running your app as a container, and the container only runs when requests come in
--> App Engine: A bit faster, but charged for the entire time it is up, so significantly more expensive

### Detailed Guide to Docker
[Docker Guide](https://robertcooper.me/post/docker-guide)

### Deploying Django on Cloud Run 
[Running Django on the Cloud Run environment - Google Cloud](https://cloud.google.com/python/django/run)

### django_settings 
#### Project Number: 169578510116
projects/169578510116/secrets/django_settings
--> Member: 169578510116@cloudbuild.gserviceaccount.com
--> Role: Secret Manager Secret Accessor

### superuser_password 
gingerCakes9292

#### Member
169578510116@cloudbuild.gserviceaccount.com
--> Role: Secret Manager Secret Accessor

#### realm-dj Service URL 
https://realm-dj-34ezrkuhla-ew.a.run.app

### Solution to custom container not connecting to port 8080 when deploying on Cloud Build 
Add this line to Dockerfile: 
`CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app`


### Stop what is currently being run on a PORT
Terminal Command: `npx kill-port 8080`

### Running App Locally 
cloud sql auth proxy must be running on port 8000
AND python manage.py runserver must be running on port 8080
--> Both need to be running 
--> And then use API on port 8080 (port python manage.py runserver is on)

Dockerfile REPLACES cloudbuild.yaml 
These are both configuration files

Examples of Configuration Files
1. Dockerfile
2. yaml
3. json 

Any changes to the Dockerfile will result in a new IMAGE being created

### Changed Continuous Deployment 
To be now from production branch rather than main

### Reverting Commits
--> Forcing a non-fastforward push to remote repo
--> Reverting and undoing commits 
(Revert a Commit)[https://gist.github.com/gunjanpatel/18f9e4d1eb609597c50c2118e416e6a6]
--> Forcefully reverting a commit will discard the deployment attempt from Cloud Run as well
1. git reset --hard <commit number>
2. git push origin -f

### Issue connecting to Cloud SQL instance through Cloud Run
Solution: Must connect Cloud SQL Instance through PRIVATE IP
--> Does not support connection through PUBLIC IP
[Quickstart: Connect from Cloud Run - Cloud SQL](https://cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-run)

For private IP paths, your application connects directly to your instance through Serverless VPC Access. This method uses a TCP socket to connect directly to the Cloud SQL instance without using the Cloud SQL Auth proxy.
--> This means that a Cloud SQL Auth proxy is not needed in production

### Actually I can use Public IP 
= It is only mySQL that needs PRIVATE IP
[Postgres Connect Instance Cloud Run](https://cloud.google.com/sql/docs/postgres/connect-instance-cloud-run)
--> Must start over and use Public IP instead, using the VPC Connector forces me to use 2 instances, which will cost much more

https://parth-vijay.medium.com/configure-postgresql-database-of-django-app-in-cloud-sql-f56ceec0fb66

https://cloud.google.com/sql/docs/postgres/connect-instance-cloud-run#console_5
https://dragonprogrammer.com/connect-django-database-cloud-sql/

#### Static File Storage with Google Cloud Storage
https://django-storages.readthedocs.io/en/latest/backends/gcloud.html

#### When connecting through python manage.py runserver 8080
= SQL Instance connects and through angeline@realmpartyapp.com

### WEDNESDAY 
1. Get docker command working
2. 
[](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy#windows)


### Postgres PORT 
5432

### PORTS
Port for Server: 8080
Host for Server: 0.0.0.0/localhost
Port for Database: 5432
Host for Database: <Public IP for SQL Instance>

The same port number used with different hosts indicate different addresses

Proxy is on the user's local machine so it is hosted at localhost 
--> But it is directed to the public ip address of the remote database

### Allowing Public IP on Cloud SQL Instance
Means that connections are only allowed to go outbound to that public ip FROM a cloud sql proxy OR from specified ip addresses
FROM PORT

### Connect to a TCP Socket using Python 
(https://cloud.google.com/sql/docs/postgres/samples/cloud-sql-postgres-sqlalchemy-connect-tcp)
--> Connect to TCP Socket where the SQL Instance with Postgres Database lies through Cloud SQL Proxy on Windows 

1. Add file with config for tcp connection 
2. Call function to connect to tcp socket for instance THROUGH Cloud SQL Proxy FROM Dockerfile

SPECIFIED
TCP specified after cloud sql proxy call is the TCP Socket for the DATABASE 
--> This is the address it is connecting TO 

connect tcp socket turns the Public IP of the Instance INTO a tcp socket that can be connected to
--> So the HOST is specified in the socket creation, and invoking Cloud SQL Proxy

DEFAULT CONFIG
The address the cloud sql proxy connects FROM is automatically the exact same PORT as the TCP Socket of the remote instance, and the HOST of the cloud sql proxy is localhost
--> This is set by DEFAULT, not needed to be specified 

### Lessons
1. Next time before doing something new, do research first, and make a step by step plan for how to use that new thing

### Django for Google Cloud
VM  
1. run.sh
```
python manage.py migrate
python manage.py collectstatic 

/usr/local/bin/gunicorn kristian.wsgi:application -w 2 -b :$PORT
```

Cloud Run
2. run.sh
```
/usr/local/bin/gunicorn base.wsgi:application -w 2 -b :8080
```

./cloud_sql_proxy -instances=realm-rn-dj:europe-west1:realm-django=tcp:8000 -credential_file=./db-proxy.json

--> To run the proxy on the Terminal

Postgres is run locally at 5432, and that is why that port is taken

Proxy is automatically connected to postgres user and postgres database locally, not the realm_django database

angeline is a new user created for the realm-django instance and granted access to the postgres database 

## Container Images
Deploy to a service for 1st time 
= Creates 1st revision 
Revisions
= Immutable 

Deploy from a container image tag 
= Will be resolved to a digest 
--> The revision will always serve this particular digest

## Connect Cloud Run to CloudSQL Postgres
https://www.youtube.com/watch?v=vMQPrVRBGdQ
--> Cloud Auth Proxy runs automatically through Cloud Run 
--> Just need to change database host to "/cloudsql/*connection name*"

## Connect to Cloud SQL Locally 
Change database "Host" in settings.py to the public IP of the Cloud SQL instance, instead of the cloudsql connection 
--> When running python manage.py migrate locally on terminal 
--> Must close DBeaver accessing the same database 

## Saving Image Data in Django 
https://www.crunchydata.com/blog/using-postgresqls-bytea-type-with-django

## Converting raw binary data of image in Django 

## Deploying backend 
Each time changes are made, backend needs to be manually deployed through Cloud Run 
--> Even though Docker is automatically built, the apis still need to be manually deployed
https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f

https://www.crunchydata.com/blog/using-postgresqls-bytea-type-with-django

https://medium.com/oceanize-geeks/react-native-expo-create-a-custom-image-upload-component-6838c00cc00e

https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f

### Models
Setting Blank to True is what allows a field to be blank when the form is sent.
https://github.com/encode/django-rest-framework/issues/6292

### Running the app locally for development
https://cloud.google.com/python/django/run#windows_2