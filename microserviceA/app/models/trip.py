from pydantic import BaseModel

class Trip(BaseModel): 
    trip_id:str
    driver_id:str
    car_id:str
    start_lon: float
    start_lat: float
    finish_lon: float
    finish_lat: float