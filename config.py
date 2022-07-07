import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# i dont know how to findmy username and password


class DatabaseURI:

    # Just change the names of your database and crendtials and all to connect to your local system
    DATABASE_NAME = "fyyur_database"
    # username = 'postgres'
    # password = 'postgres'
    url = 'localhost:8000'
    SQLALCHEMY_DATABASE_URI = "postgres://{}/{}".format(
        url, DATABASE_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#     # SQLALCHEMY_DATABASE_URI = "postgres://{}:{}@{}/{}".format(
#     # username, password, url, DATABASE_NAME)


# # TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = 'postgresql:///fyyur_database'
