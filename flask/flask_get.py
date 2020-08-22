#coding = utf-8
'''
使用flask开发get接口，访问http://127.0.0.1:5000/login获取data接口数据
'''
import json
#导入flask库
from flask import Flask
#定义一个flask对象
app = Flask(__name__)

#将login函数和路径login连接起来
#定义一个login函数
@app.route("/login")
def login():
    data = json.dumps({
        "username":"linjiejie",
        "password":"12345678"
    })
    return data

#设置主函数
if __name__ == "__main__" :
    #运行app对象
    app.run()