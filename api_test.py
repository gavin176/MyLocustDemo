import requests

def get_method():
    url='https://github.com/timeline.json'
    response = requests.get(url,verify=False)
    print(response.content)

def post_method():
    headers = {
        "xxx": "xxx",
        "xxx": "xxx"
    }
    data = {
        "email": "xxx",
        "password": "xxx"
    }
    response = requests.post("https:xxxxxx",data=data,headers=headers,verify=False)
    print(response.content)
    data = response.json()
    print("token is :",data["data"]["token"])

post_method()
