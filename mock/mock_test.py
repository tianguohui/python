#coding = utf-8
import requests
import unittest
import mock


def post_request(url,data):
    res = requests.post(url=url,data=data)
    return res

def get_request(url,data=None):
    res = requests.get(url=url,params=data)
    return res


class TestLogin(unittest.TestCase):
    #setUp和tearDown方法在每个case执行前后执行
    def setUp(self):
        print("test开始执行")

    def tearDown(self):
        print("test执行结束")

    #setUpClass和tearDownClass是在每个类class开始和结束前后执行
    @classmethod
    def setUpClass(cls):
        print("--> 测试类开始执行")

    @classmethod
    def tearDownClass(cls):
        print("--> 测试类结束执行")

    def test_01_login(self):
        url = 'http://127.0.0.1:5000/user/login'
        data = {
            "username": "test",
            "password": "test"
        }
        res = get_request(url,data).json()
        print(res)


    def test_03_mock(self):
        '''
        mock数据，使用mock出post_request的接口返回数据，可用于开发接口未完成时，测试自行模拟数据进行测试脚本开发
        语法：
            1、准备data数据
            2、通过mock.Mock(return_value=data)方法将mock得知赋给变量sucess_test
            3、将sucess_test的值赋给方法post_request
            4、将post_request方法的res
            5、通过判断res()中的值实现接口脚本开发
        '''
        url = 'http://127.0.0.1:5000/user/login'
        data = str({
            "username": "test",
            "password": "test"
        })
        data1 = {
            "username": "test",
            "password": "test"
        }
        data2 = {
            "username": "test",
            "password": "test"
        }
        data_test = 'test'
        sucess_test = mock.Mock(return_value=data_test)
        post_request = sucess_test
        res = post_request
        #判断字符串是否相等
        self.assertEqual("test",res())
        #判断字典是否相等
        self.assertDictEqual(data1,data2)
        print("-->test_03_mock，测试mock通过")


    def test_02_imooc(self):
        imooc_url = 'https://www.imooc.com/course/list'
        imooc_data = {

        }
        res = get_request(imooc_url,imooc_data).text
        print(res)

if __name__ == '__main__':
    #unittest.main()
    '''
    1、创建suite对象
    2、添加测试函数到可执行addTest函数中，添加格式：suite.addTest(测试class名称('测试def名称'))
    3、创建TextTestRunner对象runner
    4、执行runner.run(suite)
    '''
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_01_login'))
    suite.addTest(TestLogin('test_03_mock'))
    runner = unittest.TextTestRunner()
    runner.run(suite)




