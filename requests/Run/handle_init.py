#conding = utf-8
import configparser
import os
base_path = os.getcwd()
latest_path = os.path.dirname(base_path)

file_path = latest_path+"/Config/server.ini"
cg = configparser.ConfigParser()
cg.read(file_path)
data = cg.get('server','url')
print(data)