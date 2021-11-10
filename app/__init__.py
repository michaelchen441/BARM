# """Setup at app startup"""
import os
import sqlalchemy
from flask import Flask, render_template
from yaml import load, Loader
# import database as db_helper

# print("Why won't this work!!!")

def init_connection_engine():
    """ initialize database setup
    Takes in os variables from environment if on GCP
    Reads in local variables that will be ignored in public repository.
    Returns:
        pool -- a connection to GCP MySQL
    """


    # detect env local or gcp
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            os.exit()

        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST')
        )
    )

    return pool


app = Flask(__name__)
db = init_connection_engine()

# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
# from app import routes



# conn = db.connect()
# userName = "user504"
# query = "Select COUNT(*) from UserInfo where userName = '"+userName+"';"
# query_results = conn.execute(query).fetchall()
# conn.close()
# return((query_results[0][0] == 0))
# e
from app import routes

# db_helper.does_user_exist()
    # if (query_results[0][0] == 0):
    #     print("False")# False
    # else
    #     print("True")# False

# conn = db.connect()
# results = conn.execute("Select * from UserInfo")
# # we do this because results is an object, this is just a quick way to verify the content
# print([x for x in results])
