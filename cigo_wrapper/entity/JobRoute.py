import json


class JobRoute:
    arrival_time = None
    distance = None
    road_time = None

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @classmethod
    def from_json(cls, job_response):
        route = cls()
        response = job_response
        for key in response.keys():
            if key == 'arrival_time' and response[key] is not None:
                route.arrival_time = response[key]
            elif key == 'distance' and response[key] is not None:
                route.distance = response[key]
            elif key == 'road_time' and response[key] is not None:
                route.road_time = response[key]

        return route
