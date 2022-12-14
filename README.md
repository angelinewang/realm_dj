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