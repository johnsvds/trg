from app.models.driver import Driver, DriverStatus
from bson import ObjectId
import uuid

class DriverServices:

    @staticmethod
    def add_driver(args, db):
        driver = Driver(
            driver_id=uuid.uuid4().hex,
            first_name=args['first_name'],
            last_name=args['last_name'],
            license_number=args['license_number'],
            status=DriverStatus.AVAILABLE
        )
        db.drivers.insert_one(driver.dict())

    @staticmethod
    def get_driver_by_id(driver_id, db):
        driver_doc = db.drivers.find_one({'driver_id': driver_id})
        return Driver(**driver_doc).dict()
    
    @staticmethod
    def get_all_drivers(db):
        driver_docs = []
        drivers_cursor = db.drivers.find()
        for driver in drivers_cursor:
            driver_doc = Driver(**driver).dict()
            driver_docs.append(driver_doc)
        return driver_docs

    @staticmethod
    def update_driver(driver_id, args, db):
        driver = Driver(
            driver_id=driver_id,
            first_name=args['first_name'],
            last_name=args['last_name'],
            license_number=args['license_number'],
            status=DriverStatus.AVAILABLE
        )
        db.drivers.update_one({'driver_id': driver_id}, {"$set": driver.dict()})

    @staticmethod
    def delete_driver(driver_id, db):
        db.drivers.delete_one({'driver_id': driver_id})