from entity.JobAction import JobAction
from entity.JobActionType import JobActionType
from network.CigoConnect import CigoConnect
from entity.Job import Job
from entity.JobSearch import JobSearch


def cigo_api_sample():
    cc = CigoConnect(debug=True, account_id='ACCOUNT_ID',
                     auth_key='AUTH_KEY')

    print('{}'.format(cc.authenticate().text))

    """ Create Job and Job Action example """
    job = Job(date='2021-06-22', customer_first_name='Abdullah', customer_last_name='Coded',
              phone_number='+96590000000', address='building 3, street 2, block 1, Shuwaikh, Kuwait')

    job_response = cc.create_new_job(job)
    print('Job Create response: {}'.format(job_response.text))

    job_id = job_response.json()['job_id']
    action_response = cc.create_job_action(job_id,
                                           JobAction(ref_id='13', action_type=JobActionType.delivery.value,
                                                     description='delivery of grocery'))
    print('Job Action Create response: {}'.format(action_response.text))

    """ Search Job example """
    job_search = JobSearch(start_date='2021-06-15')
    job_search.end_date = '2021-06-20'
    job_ids_list = []

    try:
        job_ids_list = cc.search_job(job_search)
        print('{}'.format(job_ids_list))
    except Exception as e:
        print(e)

    """ Retrieve and Update Job examples """
    for j_id in job_ids_list:
        job = cc.retrieve_job(job_id=j_id)
        job.date = '2021-06-21'
        update_resp = cc.update_job(j_id, job)
        print('Job update: {}'.format(update_resp.text))


if __name__ == '__main__':
    cigo_api_sample()
