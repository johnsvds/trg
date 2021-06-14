import json
from models.coordinates import Coordinates
from pydantic import BaseModel

class Car(BaseModel):
    car_id:str
    driver_id:str
    trip_id:str
    speed:float = 0
    position: Coordinates

    
    def update_speed(self, speed):
        self.speed = speed

    def update_coordinates(self, position):
        self.position = position
    