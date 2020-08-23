#coding = utf-8

'''
上传文件，慕课网上传头像练习
'''
import requests
import json

url = 'https://bizapi.csdn.net/download-console-api/v1/user/checkUploadSource'
#设置file值
file = {
    "file" : ("fiddler使用问题总结.docx",open("D:/Python/fiddler使用问题总结.docx","rb")),
    "fileType" : "docx"
}
#设置cookie值，否则会报错：未登录
cookie = {
    'apsid': 'BhY2U0NzEzYjgwMjAwOTcxYzk1YTZhMGE4YjdhZDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOTEzNjc3NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxNDUwMDQ2ODk3QHFxLmNvbQAAAAAAAAAAAAAAAAAAAGVlZDdlZTYwNGFkMGFmNWRjM2I2YWU2ZDk1NmI5ZTg2yng%2BX9sAPl8%3DNz'
}
file_res = requests.options(url = url,files = file)
#数据json处理显示
json_file_res = json.dumps(file_res.json(),indent=4,ensure_ascii=False)
print(json_file_res)


