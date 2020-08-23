#coding=utf8
#导入requests库
import requests
import json
import unittest
from Base_request.base_request import request
import urllib3
urllib3.disable_warnings()

class TestRequest(unittest.TestCase):
    def test_base_request(self):
        url = "https://www.imooc.com/u/sign_list"
        data = "today_date=2020-08&schId=118521"
        #设置cookie值
        cookie = {
                "apsid" : "BhY2U0NzEzYjgwMjAwOTcxYzk1YTZhMGE4YjdhZDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOTEzNjc3NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxNDUwMDQ2ODk3QHFxLmNvbQAAAAAAAAAAAAAAAAAAAGVlZDdlZTYwNGFkMGFmNWRjM2I2YWU2ZDk1NmI5ZTg2yng%2BX9sAPl8%3DNz"
            }
        #设置header值
        header_imooc = {
                #设置数据提交格式
                'Content-Type' : 'application/x-www-form-urlencoded'
        }
        #post请求
        res1 = request.send_main('post',url,data)
        print(res1)
        #res1 = requests.post(url=url,data=data,headers = header_imooc, cookies = cookie,verify=False)
        #post_res = json.dumps(res1.json(),indent=4,ensure_ascii=False)
        #print(post_res)

if __name__ == '__main__':
        unittest.main()















