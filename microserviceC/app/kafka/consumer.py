from confluent_kafka import Consumer
from app.db_connection.mongo_connection import get_db
from app.services.tracking_services import TrackingServices
import json


consumer = Consumer({
    'bootstrap.servers': 'localhost:9094',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['trip_info'])

def consume():
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue


        db = get_db()
        trip_str = msg.value().decode('utf-8')
        trip_dict = json.loads(trip_str)

        TrackingServices.add_heartbeat(trip_dict,db)
        TrackingServices.update_drivers_trip(trip_dict,db)
        TrackingServices.update_penalty(trip_dict,db)

        

    consumer.close()