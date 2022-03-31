import requests

from cigo_wrapper.entity.Itinerary import Itinerary
from cigo_wrapper.entity.Job import Job
from cigo_wrapper.entity.JobAction import JobAction
from cigo_wrapper.entity.JobGeocoding import JobGeocoding
from cigo_wrapper.entity.JobProgress import JobProgress
from cigo_wrapper.entity.VehicleTracking import VehicleTracking


class CigoConnect:
    demo_url = 'https://demo.cigotracker.com/api/v1/{}'
    prod_url = 'https://cigotracker.com/api/v1/{}'

    def __init__(self, debug, account_id, auth_key):
        if debug:
            self.base_url = self.demo_url
        else:
            self.base_url = self.prod_url

        self.account_id = account_id
        self.auth_key = auth_key

    def authenticate(self):
        """return -> json response
        Used to verify the credentials
        """

        response = requests.get(self.base_url.format('ping'), auth=(self.account_id, self.auth_key))
        return response

    def create_new_job(self, job):
        """get a job_object and return -> json response
        default 'skip_staging = True', this will take the job directly to the proper list in Cigo
        """
        response = requests.post(self.base_url.format('jobs'), auth=(self.account_id, self.auth_key),
                                 json=job.to_json())
        return response

    def search_job(self, job_search_obj):
        """get a job_search_obj and return -> jobs ids list or raise exception"""

        response = requests.post(self.base_url.format('jobs/search'), auth=(self.account_id, self.auth_key),
                                 json=job_search_obj.to_json())

        json_response = response.json()

        if json_response['statusCode'] == 200:
            if 'in_staging' in json_response.keys() and 'post_staging' in json_response.keys():
                search_results = json_response['in_staging']['ids'] + json_response['post_staging']['ids']
                return search_results

            return json_response['ids']

        self.__raise_response_exception(response)

    def retrieve_job(self, job_id):
        """get a job_id and return -> job or raise exception"""

        response = requests.get(self.base_url.format('jobs/id/{job_id}').format(job_id=job_id),
                                auth=(self.account_id, self.auth_key))

        if response.json()['statusCode'] == 200:
            job = Job.from_json(response.json()['job'])

            a_l = response.json()['actions']
            if len(a_l) > 0:
                job.actions = []
                for action in a_l:
                    job.actions.append(JobAction.from_json(action))

            return job

        self.__raise_response_exception(response)

    def delete_job(self, job_id):
        """get a job_id and return -> json response"""

        response = requests.delete(self.base_url.format('jobs/id/{job_id}').format(job_id=job_id),
                                   auth=(self.account_id, self.auth_key))
        return response

    def update_job(self, job_id, job):
        """get a job_id and return -> json response"""

        response = requests.patch(self.base_url.format('jobs/id/{job_id}').format(job_id=job_id),
                                  auth=(self.account_id, self.auth_key), json=job.to_json())
        return response

    # Action methods
    def retrieve_job_actions(self, job_id):
        """get a job_id and return -> job actions list or raise exception"""

        response = requests.get(self.base_url.format('jobs/id/{job_id}/actions').format(job_id=job_id),
                                auth=(self.account_id, self.auth_key))

        if response.json()['statusCode'] == 200:
            a_l = response.json()['actions']
            actions = []
            if len(a_l) > 0:
                for action in a_l:
                    actions.append(JobAction.from_json(action))

            return actions

        self.__raise_response_exception(response)

    def create_job_action(self, job_id, action):
        """get a job_id, action and return -> json response"""

        response = requests.post(self.base_url.format('jobs/id/{job_id}/actions').format(job_id=job_id),
                                 auth=(self.account_id, self.auth_key), json=action.to_json())
        return response

    def delete_all_job_actions(self, job_id):
        """get a job_id and return -> json response"""

        response = requests.delete(self.base_url.format('jobs/id/{job_id}/actions').format(job_id=job_id),
                                   auth=(self.account_id, self.auth_key))
        return response

    def retrieve_a_job_action(self, job_id, action_id):
        """get a job_id, action_id and return -> job action or raise exception"""

        response = requests.get(
            self.base_url.format('jobs/id/{job_id}/actions/{action_id}').format(job_id=job_id, action_id=action_id),
            auth=(self.account_id, self.auth_key))

        if response.json()['statusCode'] == 200:
            action = JobAction.from_json(response.json()['action'])
            return action

        self.__raise_response_exception(response)

    def delete_a_job_action(self, job_id, action_id):
        """get a job_id, action_id and return -> json response"""

        response = requests.delete(
            self.base_url.format('jobs/id/{job_id}/actions/{action_id}').format(job_id=job_id, action_id=action_id),
            auth=(self.account_id, self.auth_key))

        return response

    def update_a_job_action(self, job_id, action_id, action):
        """get a job_id, action_id and return -> json response"""

        response = requests.patch(
            self.base_url.format('jobs/id/{job_id}/actions/{action_id}').format(job_id=job_id, action_id=action_id),
            auth=(self.account_id, self.auth_key), json=action.to_json())

        return response

    # Itinerary methods
    def retrieve_itineraries_by_date(self, date):
        """get an date as a string and return -> itineraries_list or raise exception"""

        response = requests.get(self.base_url.format('itineraries/date/{date}').format(date=date),
                                auth=(self.account_id, self.auth_key))

        if response.json()['statusCode'] == 200:
            itineraries = []

            i_l = response.json()['itineraries']
            if len(i_l) > 0:
                for itinerary in i_l:
                    itineraries.append(Itinerary.from_json(itinerary))

            return itineraries

        self.__raise_response_exception(response)

    def retrieve_a_itinerary(self, itinerary_id):
        """get an itinerary_id and return -> itinerary or raise exception"""

        response = requests.get(
            self.base_url.format('itineraries/id/{itinerary_id}').format(itinerary_id=itinerary_id),
            auth=(self.account_id, self.auth_key))

        if response.json()['statusCode'] == 200:
            itinerary = Itinerary.from_json(response.json()['itinerary'])
            return itinerary

        self.__raise_response_exception(response)

    def retrieve_job_latest_geolocation(self, job_id):
        """
        Retrieve the approximate geolocation of the assigned Operator.
        
        The response also contains their last known ETA and distance from 
        the Job's geolocation.
        """
        url = self.base_url.format(f'jobs/id/{job_id}/location')
        response = requests.get(url, auth=(self.account_id, self.auth_key))
        data = response.json()

        if data['statusCode'] != 200:
            return self.__raise_response_exception(response)

        job_data = data["job"]
        job = Job.from_json(job_data)

        # In job the job instance "coordinates", "progress" and "geocoding" are added from response.post_staging.%,
        # but in retrieve_job_latest_geolocation we are getting coordinates under response.%
        if job_data.get("progress"):
            job.progress = JobProgress.from_json(job_data["progress"])

        if job_data.get("coordinates"):
            job.coordinates = job_data["coordinates"]

        if job_data.get("geocoding"):
            job.geocoding = JobGeocoding.from_json(job_data["geocoding"])

        if job_data.get("vehicle_tracking"):
            job.vehicle_tracking = VehicleTracking.from_json(job_data["vehicle_tracking"])
        return job

    def __raise_response_exception(self, response):
        raise Exception('{}'.format(response.json()))
