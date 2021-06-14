from app.models.trip import Trip
from app.models.car import Car,CarStatus
from app.models.driver import Driver,DriverStatus
from app.global_components.kafka import producer
from bson import ObjectId
from os import environ, path
from dotenv import load_dotenv
import json
import uuid

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '..', '.env'))

class TripServices:

    @staticmethod
    def add_trip(args, db):
        trip=Trip(
            trip_id = uuid.uuid4().hex,
            driver_id=args['driver_id'],
            car_id=args['car_id'],
            start_lon=args['start_lon'],
            start_lat=args['start_lat'],
            finish_lon=args['finish_lon'],
            finish_lat=args['finish_lat']
        )
        driver_exists = db.drivers.find_one({'driver_id': trip.driver_id})
        car_exists = db.cars.find_one({'car_id': trip.car_id})

        if driver_exists and car_exists:
            db.trips.insert_one(trip.dict())
            db.drivers.update_one({'driver_id': trip.driver_id}, {"$set":{"status": DriverStatus.UNAVAILABLE}})
            db.cars.update_one({'car_id': trip.car_id}, {"$set":{"status": CarStatus.UNAVAILABLE}})

    @staticmethod
    def get_trip_by_id(trip_id, db):
        trip_doc = db.trips.find_one({'trip_id': trip_id})
        return Trip(**trip_doc).dict()

    @staticmethod
    def get_all_trips(db):
        trip_docs = []
        trips_cursor = db.trip.find()
        for trip in trips_cursor:
            trip_doc = Trip(**trip).dict()
            trip_docs.append(trip_doc)
        return trip_docs

    @staticmethod
    def update_trip(trip_id, args, db):
        trip=Trip(
            trip_id=trip_id,
            driver_id=args['driver_id'],
            car_id=args['car_id'],
            start_lon=args['start_lon'],
            start_lat=args['start_lat'],
            finish_lon=args['finish_lon'],
            finish_lat=args['finish_lat']
        )
        db.trips.update_one({'trip_id': trip_id}, {"$set": trip.dict()})

    @staticmethod
    def delete_trip(trip_id, db):
        db.trips.delete_one({'trip_id': trip_id})
    
    @staticmethod
    def simulate(trip_id, db):
        trip_doc = db.trips.find_one({'trip_id': trip_id})
        trip = Trip(**trip_doc).dict()
        trip_encoded = json.dumps(trip, indent=2).encode('utf-8')

        topic = environ.get('START_SIMULATION_TOPIC')

        producer.produce(topic, trip_encoded)

        # db.drivers.update_one({'_id': ObjectId(trip.driver_id)}, {"$set":{"status": DriverStatus.AVAILABLE}})
        # db.cars.update_one({'_id': ObjectId(trip.car_id)}, {"$set":{"status": CarStatus.AVAILABLE}})



        