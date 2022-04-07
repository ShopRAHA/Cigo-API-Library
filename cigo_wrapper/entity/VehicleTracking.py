import json

from cigo_wrapper.entity.JobRoute import JobRoute


class VehicleTracking:
    # it is the last known location for the vehicle assigned to fulfil this job
    coordinates = None
    last_known = None
    route_data = None

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @classmethod
    def from_json(cls, job_response):
        vehicle_tracking = cls()
        response = job_response
        for key in response.keys():
            if key == 'coordinates' and response[key] is not None:
                vehicle_tracking.coordinates = response[key]
            elif key == 'last_known' and response[key] is not None:
                vehicle_tracking.last_known = response[key]
            elif key == 'route_data' and response[key] is not None:
                vehicle_tracking.route_data = JobRoute.from_json(response[key])

        return vehicle_tracking
