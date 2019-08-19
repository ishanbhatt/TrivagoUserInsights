from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def get_amenities(self):
        r = self.client.get("/amenities?user_id=9981336825190994&limit=10")

    @task(1)
    def get_hotels(self):
        r = self.client.get("/hotels?user_id=1637496642982613300&limit=10")

"""
To be run by locust_runner.sh
./locust_runner.sh 2 > stats_logger 2 > &1
"""


class MyLocust(HttpLocust):
    task_set = UserBehavior
    stop_timeout = 120
    host = "http://localhost:5300"
