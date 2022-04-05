import json


class JobProgress:
    duration = None
    start_datetime = None
    end_datetime = None
    started = None
    finished = None

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @classmethod
    def from_json(cls, job_response):
        progress = cls()
        response = job_response
        for key in response.keys():
            if key == 'duration' and response[key] is not None:
                progress.duration = response[key]
            elif key == 'start_datetime' and response[key] is not None:
                progress.start_datetime = response[key]
            elif key == 'end_datetime' and response[key] is not None:
                progress.end_datetime = response[key]
            elif key == 'started' and response[key] is not None:
                progress.started = response[key]
            elif key == 'finished' and response[key] is not None:
                progress.finished = response[key]

        return progress
