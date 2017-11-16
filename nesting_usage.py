from locust import HttpLocust, TaskSet, task

class NestingTask(TaskSet):

    @task
    def visit_sogou(self):
        url = "https://www.sogou.com"
        print(url)
        with self.client.get(url, catch_response=True,verify=False,name="sogou") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("error")

    @task
    class SubTask(TaskSet):
        def on_start(self):
            pass

        @task(1)
        def visit_baidu(self):
            url = "https://baidu.com"
            print(url)
            with self.client.get(url,catch_response=True,verify=False,name="baidu") as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure("error")

        @task(1)
        def visit_google(self):
            url = "http://google.com"
            print(url)
            with self.client.get(url,catch_response=True,verify=False,name="google") as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure("error")

        @task(2)
        def stop(self):
            self.interrupt()

class WebsiteUser(HttpLocust):
    task_set = NestingTask
    host = "http://example.com"
    min_wait = 1000
    max_wait = 5000