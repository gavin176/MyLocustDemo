from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):

    def get_json_data(self,data):
        return data["weatherinfo"]["cityid"]

    def on_start(self):
        pass

    @task
    def query_weather(self):
        with self.client.get("/data/cityinfo/101010100.html",catch_response=True) as response:
            data = self.get_json_data(response.json())
            if data == "101010100":
                response.success()

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://www.weather.com.cn"
    min_wait = 1000
    max_wait = 5000