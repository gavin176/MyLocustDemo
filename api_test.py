import requests

def get_method():
    url='https://github.com/timeline.json'
    response = requests.get(url,verify=False)
    print(response.content)

def post_method():
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
        "email": "xxx",
        "password": "xxx"
    }
    response = requests.post("https://account-api.dji.com/apis/apprest/v1/email_login",data=data,headers=headers,verify=False)
    print(response.content)
    data = response.json()
    print("token is :",data["data"]["token"])

post_method()
