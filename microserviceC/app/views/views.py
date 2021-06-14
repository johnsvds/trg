from flask_restful import Resource, Api, reqparse
from flask import Blueprint
from bson.json_util import dumps
from app.db_connection.mongo_connection import get_db
from app.services.tracking_services import TrackingServices

api_bp = Blueprint('views', __name__)
api = Api(api_bp)

class DriverPenaltyAPI(Resource):
    def get(self, driver_id=None):
        db = get_db()
        if driver_id:
            result = TrackingServices.get_driver_penalty(driver_id, db)
        else:
            result = TrackingServices.get_all_driver_penalty(db)
        
        return result
 
api.add_resource(DriverPenaltyAPI,
                       '/api/driverpenalty',
                       '/api/driverpenalty/<string:driver_id>')