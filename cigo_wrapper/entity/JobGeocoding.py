import json


class JobGeocoding:
    validity = None
    subdivision_code = None
    country_code = None

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @classmethod
    def from_json(cls, job_response):
        geocoding = cls()
        response = job_response
        for key in response.keys():
            if key == 'validity' and response[key] is not None:
                geocoding.validity = response[key]
            elif key == 'subdivision_code' and response[key] is not None:
                geocoding.subdivision_code = response[key]
            elif key == 'country_code' and response[key] is not None:
                geocoding.country_code = response[key]

        return geocoding
