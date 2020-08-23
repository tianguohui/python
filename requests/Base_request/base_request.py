#coding = utf-8
import requests
import json

class BaseRequest:
    def send_get(self,url,data):
        res = requests.get(url=url,params=data).text
        return res

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).text
        return res

    def send_main(self, method, url, data):
        if method == 'get':
            res = self.send_get(url,data)
        elif method == 'post':
            res = self.send_post(url,data)

        try:
            res = json.loads(res)
        except:
            print("--> Error：Json Parsing Failed , This is a \"text\" file")
        return res

request = BaseRequest()



