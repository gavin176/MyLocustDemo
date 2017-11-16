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
            "DeviceId-Mc": "D0120D8C-09B1-45F6-AC5A-021BB6967A8E",
            "AppId-Mc": "djigo",
            "ClientName-Mc": "IOS-10.3.1-4.1.3",
            "Timestamp-Mc": "1499915090820",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-Hans-CN;q=1",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "DJI GO 4/4.1.3 (iPhone; iOS 10.3.1; Scale/3.00)",
            "Connection": "keep-alive",
            "InvokeId-Mc": "16C857B7-1187-45FC-891E-CCBCDE18EED1",
            "Sign-Mc": "BM8NJrplXWOwF/2lObV5CSe5yhI="
        }
        data = {
            "email":"xxx",
            "password":"xxx"
        }
        #https request need to add verify parameter
        with self.client.post("/apis/apprest/v1/email_login",data=data,headers=headers,verify=False) as response:
            data = response.json()
            print("token is :", data["data"]["token"])

class WebsiteUser(HttpLocust):
    task_set = PostTask
    host = "https://account-api.dji.com"
    min_wait = 1000
    max_wait = 5000
