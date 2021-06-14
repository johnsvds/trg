from confluent_kafka import Consumer
from simulator.simulator import Simulator
from models.car import Car
from models.coordinates import Coordinates
from models.root import Root
import json


consumer = Consumer({
    'bootstrap.servers': 'localhost:9094',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['mytopic'])

def init_simulation(trip_dict):
    start = Coordinates(
            lon=trip_dict['start_lon'], 
            lat=trip_dict['start_lat']
            )

    finish = Coordinates(
        lon=trip_dict['finish_lon'], 
        lat=trip_dict['finish_lat']
        )

    root = Root(start=start, finish=finish)

    car = Car(
        trip_id=trip_dict['trip_id'],
        driver_id=trip_dict['driver_id'], 
        car_id=trip_dict['car_id'], 
        position=start
        )
    return car,root


def consume():
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        trip_str = msg.value().decode('utf-8')
        trip_dict = json.loads(trip_str)

        car, root =init_simulation(trip_dict)

        sim = Simulator()
        sim.run(car,root,intervals=5)

    consumer.close()