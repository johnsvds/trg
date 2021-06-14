# from kafka.consumer import consumer
from kafka.producer import producer
from models.coordinates import Coordinates
from os import environ, path
from dotenv import load_dotenv
import numpy as np
import math
import time
import json

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '..', '.env'))


TRIP_INFO_TOPIC = environ.get('TRIP_INFO_TOPIC')
FINISH_SIMULATION_TOPIC = environ.get('FINISH_SIMULATION_TOPIC')

class Simulator:    
    def calculate_trip_duration(self):
        return round(np.random.normal(1000, 200))

    def calculate_speed(self, current_speed):
        additional_speed = round(np.random.normal(0, 5),1)
        if current_speed + additional_speed <0:
            current_speed = 0
        else:
            current_speed += additional_speed
        return current_speed 

    def calculate_number_of_heartbeats(self, duration, intervals):
        number_of_heartbeats = duration / intervals
        return number_of_heartbeats

    def incremental_units(self, root, number_of_heartbeats):
        inc_lon = (root.finish.lon - root.start.lon)/number_of_heartbeats
        inc_lat = (root.finish.lat - root.start.lat)/number_of_heartbeats
        return inc_lon, inc_lat
        

    def calculate_position(self, position, inc_lon, inc_lat):
        position.lon += inc_lon 
        position.lat += inc_lat
        return Coordinates(lon=position.lon, lat=position.lat)

    def broadcast_car_info(self, car):
        car_dict = car.dict()
        car_encoded = json.dumps(car_dict, indent=2).encode('UTF-8')
        producer.produce(TRIP_INFO_TOPIC,car_encoded)
        producer.flush()
    
    def broadcast_simulation_stop(self,car):
        car_dict = car.dict()
        car_encoded = json.dumps(car_dict, indent=2).encode('UTF-8')
        producer.produce(FINISH_SIMULATION_TOPIC,car_encoded)
        producer.flush()

    def run(self, car, root, intervals):
        duration = self.calculate_trip_duration()
        number_of_heartbeats = self.calculate_number_of_heartbeats(duration, intervals)
        inc_lon, inc_lat = self.incremental_units(root, number_of_heartbeats)
        print("Running..")
        while abs(car.position.lon- root.finish.lon)> 10**-4 or abs(car.position.lon - root.finish.lon)> 10**-4:
            car.update_speed(self.calculate_speed(car.speed))
            car.update_coordinates(self.calculate_position(car.position, inc_lon, inc_lat))
            self.broadcast_car_info(car)
            time.sleep(intervals)
        self.broadcast_simulation_stop(car)
        print("Finished")
            

    