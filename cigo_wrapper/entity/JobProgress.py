class JobProgress:
    duration = None
    start_datetime = None
    end_datetime = None
    started = None
    finished = None

    @classmethod
    def from_json(cls, job_response):
        progress = cls()
        response_dic = job_response
        for key in response_dic.keys():
            if key == 'duration' and response_dic[key] is not None:
                progress.duration = response_dic[key]
            elif key == 'start_datetime' and response_dic[key] is not None:
                progress.start_datetime = response_dic[key]
            elif key == 'end_datetime' and response_dic[key] is not None:
                progress.end_datetime = response_dic[key]
            elif key == 'started' and response_dic[key] is not None:
                progress.started = response_dic[key]
            elif key == 'finished' and response_dic[key] is not None:
                progress.finished = response_dic[key]

        return progress
