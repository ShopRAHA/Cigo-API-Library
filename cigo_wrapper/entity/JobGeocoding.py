class JobGeocoding:
    validity = None
    subdivision_code = None
    country_code = None

    @classmethod
    def from_json(cls, job_response):
        geocoding = cls()
        response_dic = job_response
        for key in response_dic.keys():
            if key == 'validity' and response_dic[key] is not None:
                geocoding.validity = response_dic[key]
            elif key == 'subdivision_code' and response_dic[key] is not None:
                geocoding.subdivision_code = response_dic[key]
            elif key == 'country_code' and response_dic[key] is not None:
                geocoding.country_code = response_dic[key]

        return geocoding
