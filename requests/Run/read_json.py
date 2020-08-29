#coding = utf-8
import os
import json
base_path = os.getcwd()
latest_path = os.path.dirname(base_path)

def open_jsonfile(file_path=None):
    '''
    1、读取json文件
    :param file_path: 文件路径，只传递json文件相对路径
    :return: 返回json文件对象
    '''
    if file_path == None:
        file_path = latest_path + "/Config/result_imooc.json"
    else:
        file_path=latest_path+file_path
    with open(file=file_path , encoding="UTF-8") as file:
        data = json.load(file)
    return data

def read_json_value(key,file=None):
    '''
    1、读取json中key值对应的json数据
    :param key: json数据对应的关键字
    :param file: 文件名称（相对路径）
    :return:返回key值对应的json数据
    '''
    value = open_jsonfile(file_path=file)[key]
    return value



