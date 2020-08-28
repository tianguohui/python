#coding=utf8
'''
1、使用unittest和requests结合
2、将预期结果写入json文件，读取u_sign_list.json文件内容，使用mock方法mock文件内容作为预期结果
3、通过self.assertEqual(res1['result'],0)判断预期结果是否正确
4、网上下载HTMLTestRunner.py文件，放到python安装路径下，具体路径为：\Lib\site-packages
5、导入模块，使用HTMLTestRunner.HTMLTestRunner()方法，生成测试报告
'''

import unittest
import mock
#导入Base_request目录中base_request文件中request方法
from Base_request.base_request import request
#导入HTMLTestRunner模块
import HTMLTestRunner
import urllib3
urllib3.disable_warnings()
import sys
import os
import json
#获取当前目录：D:/Python/requests/unittest
base_path = os.getcwd()
sys.path.append(base_path)
#获取上一级目录：D:/Python/requests
latest_path = os.path.dirname(base_path)

'''
读取预期结果json文件内容，json文件名为：u_sign_list.json
返回json数据
'''
def read_json():
    with open(latest_path+'/Config/u_sign_list.json','rb') as file:
        return json.load(file)

hosts = 'https://www.imooc.com'
class TestRequest(unittest.TestCase):
    '''
    调用自己封装的request方法：send_main()，调用post方法
    具体语句：request.send_main('post',url,data)
    '''
    def test_signlist(self):
        url = hosts + "/u/sign_list"
        data = "today_date=2020-08&schId=118521"
        #mock数据：预期结果
        sign_data= mock.Mock(return_value=read_json())
        request.send_main = sign_data
        #post请求
        res1 = request.send_main('post',url,data)
        #判断返回结果中result的值是否等于0，返回结果为：{'result': -11, 'data': '', 'msg': '没有登录'}
        #mock后的数据为：json文件中的内容
        self.assertEqual(res1['result'],0)
        #print(res1)

    '''
    1、使用get方法，请求接口数据
    2、请求结果为：{'result': 0, 'data': {'remind': 4}, 'msg': '成功'}
    '''
    def test_loding(self):
        url =hosts+ '/u/loading'
        print(url)
        res = request.send_main('get', url=url, data=None)
        self.assertEqual(res['result'],0)
        #print(res)

'''
1、	下载HTMLTestRunner.py文件，放入python安装路径中，具体路径为：D:\InstallApp\Python3.7.8\Lib\site-packages 
2、	下载地址：百度云盘链接：https://pan.baidu.com/s/1y2lvQvJnPJlwPK935O100w 。提取码：4k3l
3、	导入HTMLTestRunner模块
4、	使用unittest和HTMLTestRunner结合，生成测试报告
5、	用法：HTMLTestRunner.HTMLTestRunner(stream=’文件路径+文件名称’,title="html文件标题",description="描述信息")
6、关闭文件：file.close()
'''

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRequest("test_signlist"))
    suite.addTest(TestRequest("test_loding"))
    #html_path = 'D:/Python/requests/Report/test_base_request.html'
    html_path = latest_path+'/Report/htmltestrunner_case.html'
    print(html_path)
    with open(html_path,'wb') as file:
        set_runenr = HTMLTestRunner.HTMLTestRunner(stream=file,title="测试报告",description="测试生产测试报告")
        set_runenr.run(suite)
    file.close()

