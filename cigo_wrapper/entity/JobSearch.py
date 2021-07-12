import json


# All dates are in ISO-8601 format
class JobSearch:
    # If end_date is not set it will automatically be assigned to start_date
    # start_date and end_date can be a period of 30 days max
    end_date = None

    status = None
    first_name = None
    last_name = None
    phone_number = None
    quick_desc = None
    invoice_number = None
    shipping_barcode = None
    reference_id = None
    confirmation_status = None
    branch_id = None
    distribution_center_id = None

    def __init__(self, start_date='tbd'):
        self.start_date = start_date

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))
