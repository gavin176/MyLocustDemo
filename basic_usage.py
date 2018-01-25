from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):

    def on_start(self):
        pass

    @task(2)
    def visit_baidu(self):
        url = "http://baidu.com"
        print(url)
        with self.client.get(url,catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("error")

    @task(1)
    def visit_google(self):
        url = "http://google.com"
        print(url)
        with self.client.get(url,catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("error")

class PostTask(TaskSet):

    @task
    def post_method(self):
        headers = {
            "xxx": "xxx",
            "xxx": "xxx",
        }
        data = {
            "email":"xxx",
            "password":"xxx"
        }
        #https request need to add verify parameter
        with self.client.post("xxx",data=data,headers=headers,verify=False) as response:
            data = response.json()
            print("token is :", data["data"]["token"])

class WebsiteUser(HttpLocust):
    task_set = PostTask
    host = "https://xxx.com"
    min_wait = 1000
    max_wait = 5000
