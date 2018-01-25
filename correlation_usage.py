from locust import HttpLocust, TaskSet, task

class CorrelationTask(TaskSet):

    def on_start(self):
        self.token = self.get_token()

    def get_token(self):
        headers = {
            "xxx": "xxx",
            "xxx": "xxx",
        }
        data = {
            "email":"xxx",
            "password":"xxx"
        }
        #https request need to add verify parameter
        response = self.client.post("xxx",data=data,headers=headers,verify=False)
        json_data = response.json()
        return json_data["data"]["token"]

    @task
    def use_token(self):
        print(self.token)

class WebsiteUser(HttpLocust):
    task_set = CorrelationTask
    host = "https://xxx.com"
    min_wait = 1000
    max_wait = 5000
