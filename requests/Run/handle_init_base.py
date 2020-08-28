#conding = utf-8
'''
通过configparser库读取配置文件server.ini文件
'''
import configparser
import os
base_path = os.getcwd()
latest_path = os.path.dirname(base_path)

file_path = latest_path+"/Config/server.ini"
#定义configparser对象
cg = configparser.ConfigParser()
#读取文件
cg.read(file_path)
#获取文件下server模块下url的值
data = cg.get('server','url')
print(data)