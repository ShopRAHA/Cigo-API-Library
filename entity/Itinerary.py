import json


class Itinerary:
    itinerary_id = None
    date = None
    planned_departure_datetime = None
    start_location = None
    end_location = None
    round_trip = None
    route_metrics = None
    route_options = None
    vehicle = None
    operators = None
    stops_count = None
    stops = None

    @classmethod
    def from_json(cls, itinerary_response):
        itinerary = cls()
        response_dic = itinerary_response

        for key in response_dic.keys():
            if key == 'itinerary_id':
                itinerary.itinerary_id = response_dic[key]
            elif key == 'date':
                itinerary.date = response_dic[key]
            elif key == 'planned_departure_datetime':
                itinerary.planned_departure_datetime = response_dic[key]
            elif key == 'start_location':
                itinerary.start_location = response_dic[key]
            elif key == 'end_location':
                itinerary.end_location = response_dic[key]
            elif key == 'round_trip':
                itinerary.round_trip = response_dic[key]
            elif key == 'route_metrics':
                itinerary.route_metrics = response_dic[key]
            elif key == 'route_options':
                itinerary.route_options = response_dic[key]
            elif key == 'vehicle':
                itinerary.vehicle = response_dic[key]
            elif key == 'operators':
                itinerary.operators = response_dic[key]
            elif key == 'stops_count':
                itinerary.stops_count = response_dic[key]
            elif key == 'stops':
                itinerary.stops = response_dic[key]

        return itinerary
