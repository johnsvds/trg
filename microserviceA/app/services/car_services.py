from app.models.car import Car,CarStatus
from bson import ObjectId
import uuid

class CarServices:

    @staticmethod
    def add_car(args, db):
        car = Car(
            car_id=uuid.uuid4().hex,
            brand=args['brand'],
            model=args['model'],
            license_plate=args['license_plate'],
            status = CarStatus.AVAILABLE
        )
        db.cars.insert_one(car.dict())

    @staticmethod
    def get_car_by_id(car_id, db):
        car_doc =  db.cars.find_one({'car_id': car_id})
        return Car(**car_doc).dict()
    
    @staticmethod
    def get_all_cars(db):
        car_docs=[]
        cars_cursor = db.cars.find()
        for car in cars_cursor:
            car_doc = Car(**car).dict()
            car_docs.append(car_doc)
        return car_docs

    @staticmethod
    def update_car(car_id, args, db):
        car = Car(
            car_id=car_id,
            brand=args['brand'],
            model=args['model'],
            license_plate=args['license_plate'],
            status = CarStatus.AVAILABLE
        )
        db.cars.update_one({'car_id': car_id}, {"$set": car.dict()})

    @staticmethod
    def delete_car(car_id, db):
        db.cars.delete_one({'car_id': car_id})
    
