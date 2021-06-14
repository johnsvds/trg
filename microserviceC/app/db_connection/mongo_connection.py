from pymongo import MongoClient
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '..', '.env'))


username = environ.get('DB_USERNAME')
password = environ.get('DB_PASSWORD')
host = environ.get('DB_HOST')
# db_name = environ.get('DB_NAME')

uri = "mongodb://%s:%s@%s" % (username, password, host)

def get_db():
    client = MongoClient(uri)
    return client.penalty

