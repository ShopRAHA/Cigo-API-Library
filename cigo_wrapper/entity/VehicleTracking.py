class VehicleTracking:
    coordinates = None
    last_known = None
    route_data = None

    @classmethod
    def from_json(cls, job_response):
        vehicle_tracking = cls()
        response_dic = job_response
        for key in response_dic.keys():
            if key == 'coordinates' and response_dic[key] is not None:
                vehicle_tracking.coordinates = response_dic[key]
            elif key == 'last_known' and response_dic[key] is not None:
                vehicle_tracking.last_known = response_dic[key]
            elif key == 'route_data' and response_dic[key] is not None:
                vehicle_tracking.route_data = response_dic[key]

        return vehicle_tracking
