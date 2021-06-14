from confluent_kafka import Producer
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '..', '.env'))
BOOTSTRAP_SERVER = environ.get('BOOTSTRAP_SERVER')

producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVER})
