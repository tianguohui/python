'''
    封装基础请求方法
'''
#coding = utf-8
import requests
from Run.handle_ini import handlini
import json

class BaseRequest:
    '''
     get方法，传入url，data参数，返回text格式结果
    '''
    def send_get(self,url,data):
        res = requests.get(url=url,params=data).text
        return res

    '''
    post方法，传入url,data参数，返回text格式结果
    '''
    def send_post(self,url,data):
        res = requests.post(url=url,data=data).text
        return res

    '''
    1、运行函数，判断method方法，根据method的值调用不同的方法，返回不同的结果
    2、通过json.loads()判断结果是否为json格式数据，如果是，则重新复制，否则输出不是json格式提示语
    3、返回res请求结果
    '''
    def send_main(self, method, url, data):
        '''
        使用handlini.get_ini_value()读取配置文件server.ini文件中的参数，用到接口请求中
        :param method: 传入请求方式，get,post
        :param url: 请求地址
        :param data: 请求参数
        :return: 返回接口请求结果
        '''
        base_url = handlini.get_ini_value(option='server', key='url')
        if "http" not in url:
            url = base_url+url
        #print(url)
        if method == 'get':
            res = self.send_get(url,data)
        elif method == 'post':
            res = self.send_post(url,data)
        try:
            res = json.loads(res)
        except:
            #res = json.loads(res)
            print("--> Error：Json Parsing Failed , This is a \"text\" file")
        return res

#实例化方法request，其他文件可以直接调用
request = BaseRequest()

'''
if __name__ == '__main__':
    request.send_main('get','http://ww.bai.com/login','{"username":"test"}')
    request.send_main('get','/login','{"username":"test"}')
'''



