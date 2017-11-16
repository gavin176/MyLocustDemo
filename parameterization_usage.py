from locust import HttpLocust, TaskSet, task
import queue

class ListTask(TaskSet):

    def on_start(self):
        self.index = 0

    def get_json_data(self,data):
        return data["weatherinfo"]["cityid"]

    @task
    def query_weather(self):
        url = "/data/cityinfo/"+self.locust.share_data_list[self.index]+".html"
        temp_index = self.index
        self.index = (self.index + 1) % len(self.locust.share_data_list)
        with self.client.get(url,catch_response=True) as response:
            data = self.get_json_data(response.json())
            if data == self.locust.share_data_list[temp_index]:
                response.success()
            else:
                response.failure("error")

class QueueTask_NoRepeat(TaskSet):

    def on_start(self):
        self.index = 0

    def get_json_data(self,data):
        return data["weatherinfo"]["cityid"]

    @task
    def query_weather(self):
        try:
            user_data = self.locust.share_data_queue.get()
        except queue.Empty:
            exit(0)
        url = "/data/cityinfo/"+user_data+".html"
        with self.client.get(url,catch_response=True) as response:
            data = self.get_json_data(response.json())
            if data == user_data:
                response.success()
            else:
                response.failure("error")


class QueueTask_Repeat(TaskSet):

    def on_start(self):
        self.index = 0

    def get_json_data(self,data):
        return data["weatherinfo"]["cityid"]

    @task
    def query_weather(self):
        try:
            user_data = self.locust.share_data_queue.get()
        except queue.Empty:
            exit(0)
        url = "/data/cityinfo/"+user_data+".html"
        with self.client.get(url,catch_response=True) as response:
            data = self.get_json_data(response.json())
            if data == user_data:
                response.success()
            else:
                response.failure("error")
        self.locust.share_data_queue.put_nowait(user_data)

class WebsiteUser(HttpLocust):
    share_data_list = ["101010100","101320101","101050101","101060101"]
    share_data_queue = queue.Queue()
    for item in share_data_list:
        share_data_queue.put_nowait(item)

    host = "http://www.weather.com.cn"
    min_wait = 1000
    max_wait = 5000
    task_set = QueueTask_Repeat