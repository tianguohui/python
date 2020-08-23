#coding = uft-8
import requests
#导入hashlib库
import hashlib

#对data的值进行加密，并输出原来的data值与加密后的值
data = "111111"
data_md5 = hashlib.md5()
data_md5.update(data.encode('utf-8'))
data_res = data_md5.hexdigest()
print(data)
print(data_res)

