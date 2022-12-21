# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from google.cloud.sql.connector import Connector, IPTypes


# # Python Connector database connection function
# def getconn():
#     with Connector() as connector:
#         conn = connector.connect(
#             "realm-rn-dj:europe-west1:realm-django",  # Cloud SQL Instance Connection Name
#             "pg8000",
#             user="postgres",
#             password="blueLilacs8830",
#             db="realm_django",
#             ip_type=IPTypes.PUBLIC  # IPTypes.PRIVATE for private IP
#         )
#         return conn


# app = Flask(__name__)

# # configure Flask-SQLAlchemy to use Python Connector
# # postgres: blueLilacs8830@35.195.57.236: 5432/realm_django
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pg8000://"
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
#     "creator": getconn
# }

# db = SQLAlchemy(app)

import os

import sqlalchemy


# connect_tcp_socket initializes a TCP connection pool
# for a Cloud SQL instance of MySQL.
def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.
    # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
    db_host = os.environ["INSTANCE_HOST"]
    db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
    db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
    db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    db_port = os.environ["DB_PORT"]  # e.g. 3306

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL.create(
            drivername="postgres+pg8000",
            username=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
            database=db_name,
        ),
        # ...
    )
    return pool
