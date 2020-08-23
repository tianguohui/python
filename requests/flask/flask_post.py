#coding = utf-8
'''
使用flask开发post接口，访问http://127.0.0.1:5000/post/login获取data接口数据
'''
import json
#导入flask库
from flask import Flask
from flask import request
#定义一个flask对象
app = Flask(__name__)
'''
将login函数和路径/post/login连接起来
定义一个login函数，请求方式指定为post，methods=['post']
通过请求http://127.0.0.1:5000/post/login?username=test&password=123456获取username和password的数据
'''
@app.route("/login",methods=['post'])
def login():
    username=request.args.get('username')
    password=request.args.get('password')
    if username and password :
        data = json.dumps({
            "username":username,
            "password":password
        })
    return data

'''
通过请求http://127.0.0.1:5000/user/login?username=test&password=test
判断username是否等于test，password是否等于test，如果两者都满足条件，则输出data数据，否则输出“账号/密码不正确！”
利用flask的requests方法，获取请求接口的数据，与程序设置的进行对比
'''
@app.route("/user/login",methods=['get'])
def user_login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'test' and password == 'test':
        data = json.dumps({
            "username":username,
            "password":password,
            "code": 200,
            "masge": "登录成功"
        },
        ensure_ascii=False
        )
    else:
        data = json.dumps({
            "code": 200,
            "masge": "账号/密码不正确！"
        },
        ensure_ascii=False
        )
    return data

#设置主函数
if __name__ == "__main__" :
    #运行app对象
    app.run()