import json

from cigo_wrapper.entity.JobGeocoding import JobGeocoding
from cigo_wrapper.entity.JobProgress import JobProgress
from cigo_wrapper.entity.VehicleTracking import VehicleTracking


# All dates are in ISO-8601 format


class Job:
    # In the documentation the create request used 'type' as the key but in the response it uses 'job_type'
    type = None
    quick_desc = None
    confirmation_status = None
    email = None
    # [0.0, 0.0]
    coordinates = None
    apartment = None
    postal_code = None
    balance_owed = None
    comment = None
    # {"start": "0:00 AM", "end": "0:00 AM"}
    time_frame = None
    # ['124', ]
    invoices = None
    # order reference id
    reference_id = None
    customer_reference_id = None

    actions = None

    # Data from Cigo
    job_id = None
    status = None

    # post_staging attributes
    tracking = None
    progress = None
    scheduling = None
    geocoding = None
    digital_signature = None
    payment_collection = None
    review = None

    def __init__(self, date=None, customer_first_name="", customer_last_name="", phone_number="", address="",
                 skip_staging=True):
        # Job created will skip the staging area (Import Tool) if True
        self.skip_staging = skip_staging

        self.date = date
        self.first_name = customer_first_name
        self.last_name = customer_last_name

        self.phone_number = phone_number
        # Cigo use the mobile_number to send an sms with the tracking code
        self.mobile_number = phone_number

        self.address = address

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @classmethod
    def from_geocoding(cls, job_response):
        response_dic = job_response
        job = cls()
        for key in response_dic.keys():
            if key == 'job_id' and response_dic[key] is not None:
                job.job_id = response_dic[key]
            elif key == 'status' and response_dic[key] is not None:
                job.status = response_dic[key]
            elif key == 'progress' and response_dic[key] is not None:
                job.progress = JobProgress.from_json(response_dic[key])
            elif key == 'coordinates' and response_dic[key] is not None:
                job.coordinates = response_dic[key]  # is the location of the Job (the target location)
            elif key == 'geocoding' and response_dic[key] is not None:
                job.geocoding = JobGeocoding.from_json(response_dic[key])
            elif key == 'vehicle_tracking' and response_dic[key] is not None:
                job.vehicle_tracking = VehicleTracking.from_json(response_dic[key])
        return job

    @classmethod
    def from_json(cls, job_response):
        response_dic = job_response
        job = cls(date=response_dic['date'], customer_first_name=response_dic['first_name'],
                  customer_last_name=response_dic['last_name'],
                  phone_number=response_dic['phone_number'],
                  address=response_dic['address'])

        for key in response_dic.keys():
            if key == 'job_id' and response_dic[key] is not None:
                job.job_id = response_dic[key]
            elif key == 'job_type' and response_dic[key] is not None:
                job.type = response_dic[key]
            elif key == 'status' and response_dic[key] is not None:
                job.status = response_dic[key]
            elif key == 'quick_desc' and response_dic[key] is not None:
                job.quick_desc = response_dic[key]
            elif key == 'confirmation_status' and response_dic[key] is not None:
                job.confirmation_status = response_dic[key]
            elif key == 'mobile_number' and response_dic[key] is not None:
                job.mobile_number = response_dic[key]
            elif key == 'email' and response_dic[key] is not None:
                job.email = response_dic[key]
            elif key == 'apartment' and response_dic[key] is not None:
                job.apartment = response_dic[key]
            elif key == 'postal_code' and response_dic[key] is not None:
                job.postal_code = response_dic[key]
            elif key == 'time_preference' and response_dic[key] != 'None' and response_dic[key] is not None:
                job.time_preference = response_dic[key]
            elif key == 'balance_owed' and response_dic[key] is not None:
                job.balance_owed = response_dic[key]
            elif key == 'comment' and response_dic[key] is not None:
                job.comment = response_dic[key]
            elif key == 'branch_id' and response_dic[key] is not None:
                job.branch_id = response_dic[key]
            elif key == 'distribution_center_id' and response_dic[key] is not None:
                job.distribution_center_id = response_dic[key]
            elif key == 'time_frame' and response_dic[key] is not None:
                if response_dic[key]['start'] is not None and response_dic[key]['end'] is not None:
                    job.time_frame = response_dic[key]
            elif key == 'invoices' and response_dic[key] is not None:
                job.invoices = response_dic[key]
            elif key == 'reference_id' and response_dic[key] is not None:
                job.reference_id = response_dic[key]
            elif key == 'customer_reference_id' and response_dic[key] is not None:
                job.customer_reference_id = response_dic[key]
            elif key == 'post_staging' and response_dic[key] is not None:
                for i_key in response_dic[key]:
                    if i_key == 'tracking' and response_dic[key][i_key] is not None:
                        job.tracking = response_dic[key][i_key]
                    elif i_key == 'progress' and response_dic[key][i_key] is not None:
                        job.progress = JobProgress.from_json(response_dic[key][i_key])
                    elif i_key == 'scheduling' and response_dic[key][i_key] is not None:
                        job.scheduling = response_dic[key][i_key]
                    elif i_key == 'coordinates' and response_dic[key][i_key] is not None:
                        job.coordinates = response_dic[key][i_key]
                    elif i_key == 'geocoding' and response_dic[key][i_key] is not None:
                        job.geocoding = JobGeocoding.from_json(response_dic[key][i_key])
                    elif i_key == 'digital_signature' and response_dic[key][i_key] is not None:
                        job.digital_signature = response_dic[key][i_key]
                    elif i_key == 'payment_collection' and response_dic[key][i_key] is not None:
                        job.payment_collection = response_dic[key][i_key]
                    elif i_key == 'review' and response_dic[key][i_key] is not None:
                        job.review = response_dic[key][i_key]

        return job
