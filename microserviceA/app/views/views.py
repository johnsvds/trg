from flask_restful import Resource, Api, reqparse
from flask import Blueprint
from app.global_components.parser import Parser
from bson.json_util import dumps
from app.services.car_services import CarServices
from app.services.driver_services import DriverServices
from app.services.trip_services import TripServices
from app.db_connection.mongo_connection import get_db

api_bp = Blueprint('views', __name__)
api = Api(api_bp)

car_parser = reqparse.RequestParser()
car_parser = Parser.car_parser(car_parser)

driver_parser = reqparse.RequestParser()
driver_parser = Parser.driver_parser(driver_parser)

trip_parser = reqparse.RequestParser()
trip_parser = Parser.trip_parser(trip_parser)

class DriverAPI(Resource):
    
    def get(self, driver_id=None):
        db = get_db()
        if driver_id:
            result = DriverServices.get_driver_by_id(driver_id, db)
        else:
            result = DriverServices.get_all_drivers(db)

        return result

    def post(self):
        db = get_db()
        args = driver_parser.parse_args()
        result = DriverServices.add_driver(args, db)

        return result

    def put(self, driver_id=None):
        db = get_db()
        if driver_id:
            args = driver_parser.parse_args()
            DriverServices.update_driver(driver_id, args, db)
            
    def delete(self, driver_id=None):
        db = get_db()
        if driver_id:
            DriverServices.delete_driver(driver_id, db)


api.add_resource(DriverAPI,
                       '/api/drivers',
                       '/api/driver/<string:driver_id>')


class CarAPI(Resource):
    def get(self, car_id=None):
        db = get_db()
        if car_id:
            result = CarServices.get_car_by_id(car_id, db)
        else:
            result = CarServices.get_all_cars(db)
        return result

    def post(self):
        db = get_db()
        args = car_parser.parse_args()
        result = CarServices.add_car(args, db)

        return result

    def put(self, car_id=None):
        db = get_db()
        if car_id:
            args = car_parser.parse_args()
            CarServices.update_car(car_id, args, db)

    def delete(self, car_id=None):
        db = get_db()
        if car_id:
            CarServices.delete_car(car_id, db)



api.add_resource(CarAPI,
                       '/api/cars',
                       '/api/car/<string:car_id>')


class TripAPI(Resource):
    def get(self, trip_id=None):
        db = get_db()
        if trip_id:
            result = TripServices.get_trip_by_id(trip_id, db)
        else:
            result = TripServices.get_all_trips(db)

        return result

    def post(self):
        db = get_db()
        args = trip_parser.parse_args()
        result = TripServices.add_trip(args, db)

        return result
    def put(self,trip_id=None):
        db = get_db()
        if trip_id:
            args = trip_parser.parse_args()
            TripServices.update_trip(trip_id, args, db)

    def delete(self, trip_id=None):
        db = get_db()
        if trip_id:
            TripServices.delete_trip(trip_id, db)


api.add_resource(TripAPI,
                       '/api/trips',
                       '/api/trip/<string:trip_id>')


class TripStatusAPI(Resource):
    def get(self, trip_id=None):
        db = get_db()
        TripServices.simulate(trip_id, db)
 


api.add_resource(TripStatusAPI,
                       '/api/tripstatus',
                       '/api/tripstatus/<string:trip_id>')
