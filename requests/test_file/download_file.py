#coding = utf-8
import requests
import json

'''
requests测试下载慕课网安卓安装包，通过open，write写入到本地磁盘中
imooc_url通过fiddler抓包，获取下载地址，本次下载指定版本，将版本作为imooc_data信息传入get方法中
'''
imooc_url = 'http://file.mukewang.com/apk/app/120/1597322853/imooc7.3.910102001android.apk'
imooc_data = {
    'version': '1597322858'
}
res = requests.get(url=imooc_url,params=imooc_data)
with open('imooc_appdown.apk','wb') as file:
    file.write(res.content)
print(res)

'''
requests测试下载百度云盘安装包，通过open，write写入到本地磁盘中
baidu_url通过fiddler抓包，获取下载地址，本次下载没有跟版本信息，只有一个url
'''
baidu_url = 'https://wppkg.baidupcs.com/issue/netdisk/apk/BaiduNetdisk_10.1.72.apk'
baidu_res = requests.get(baidu_url)
with open('baiduyunpan.apk','wb') as baidu_file:
    baidu_file.write(baidu_res.content)
print(baidu_res)





