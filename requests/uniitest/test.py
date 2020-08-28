import requests
from Base_request.base_request import request
import json
url = 'https://www.imooc.com/u/loading'
res = request.send_main('get',url=url,data=None)
#res = json.loads(res)
print(res)