#coding = utf-8
import requests
url = 'http://127.0.0.1:5000/user/login'
data = {
    'username': 'test',
    'password': 'test'
}

res = requests.get(url=url,data=data).text
print(res)

