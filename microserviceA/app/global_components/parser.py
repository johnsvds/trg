class Parser:
    @staticmethod
    def driver_parser(parser):
        parser.add_argument("first_name", type=str)
        parser.add_argument("last_name", type=str)
        parser.add_argument("license_number", type=str)

        return parser

    @staticmethod
    def car_parser(parser):
        parser.add_argument("brand", type=str)
        parser.add_argument("model", type=str)
        parser.add_argument("license_plate", type=str)

        return parser

    @staticmethod
    def trip_parser(parser):
        parser.add_argument("driver_id", type=str)
        parser.add_argument("car_id", type=str)
        parser.add_argument("start_lon", type=float)
        parser.add_argument("start_lat", type=float)
        parser.add_argument("finish_lon", type=float)
        parser.add_argument("finish_lat", type=float)

        return parser