from pydantic import BaseModel
from app.models.car import Car
from app.models.driver import Driver

class Trip(BaseModel):
    trip_id:str
    car:Car
    driver:Driver

