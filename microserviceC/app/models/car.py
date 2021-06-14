import json
from app.models.coordinates import Coordinates
from pydantic import BaseModel

class Car(BaseModel):
    car_id:str
    speed:float
    position: Coordinates
    