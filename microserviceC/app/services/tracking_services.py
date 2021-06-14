from app.models.car import Car
from app.models.driver import Driver
from app.models.trip import Trip
from app.Dto.car import CarDTO
from bson import ObjectId

class TrackingServices:

    @staticmethod
    def add_heartbeat(trip_dict, db):
        car = Car(
            car_id=trip_dict['car_id'],
            speed=trip_dict['speed'],
            position=trip_dict['position']
        )

        driver = Driver(
            driver_id=trip_dict['driver_id']
        )

        trip = Trip(
            trip_id=trip_dict['trip_id'],
            driver=driver,
            car=car
        )

        car_dto = CarDTO(
            speed=car.speed,
            position =car.position
        )

        db.trips.update_one({
            "trip_id":trip.trip_id, "trip.driver_id":driver.driver_id, "trip.car_id":car.car_id
        },{
            "$push": {"trip.heartbeats":car_dto.dict()}
        }, upsert=True)
    


    @staticmethod
    def update_drivers_trip(trip_dict, db):
        car = Car(
            car_id=trip_dict['car_id'],
            speed=trip_dict['speed'],
            position=trip_dict['position']
        )

        driver = Driver(
            driver_id=trip_dict['driver_id']
        )

        trip = Trip(
            trip_id=trip_dict['trip_id'],
            driver=driver,
            car=car
        )

        trip_exists = db.drivers.find_one({"driver_id":driver.driver_id,"trip": trip.trip_id})
        if not trip_exists:
            driver_exists = db.drivers.find_one({"driver_id":driver.driver_id})
            if not driver_exists:
                db.drivers.insert_one(driver.dict())
                db.drivers.update_one({
                    "driver_id":driver.driver_id
                },{
                    "$push": {"trip":trip.trip_id}
                }, upsert=True)
            else:
                db.drivers.update_one({
                    "driver_id":driver.driver_id
                },{
                    "$push": {"trip":trip.trip_id}
                }, upsert=True)

    
    
    @staticmethod
    def update_penalty(trip_dict, db):
        car = Car(
            car_id=trip_dict['car_id'],
            speed=trip_dict['speed'],
            position=trip_dict['position']
        )

        driver = Driver(
            driver_id=trip_dict['driver_id']
        )


        penalty=0
        if car.speed>100:
            penalty = 5*(car.speed - 100)
        elif car.speed>60:
            penalty = 2*(car.speed - 80)
        elif car.speed>50:
            penalty = 1*(car.speed - 60)


        db.drivers.update_one({
                "driver_id":driver.driver_id
            },{
                "$inc": {"penalty":penalty}
            })


    @staticmethod
    def get_driver_penalty(driver_id, db):
        driver_doc = db.drivers.find_one({'driver_id':driver_id})
        return Driver(**driver_doc).dict()

    @staticmethod
    def get_all_driver_penalty(db):
        driver_docs=[]
        drivers_cursor = db.drivers.find()
        for driver in drivers_cursor:
            driver_doc = Driver(**driver).dict()
            driver_docs.append(driver_doc)
        return driver_docs

