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
