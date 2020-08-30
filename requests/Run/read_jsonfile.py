#coding = utf-8
from Run.read_json import *
import os
import json
base_path = os.getcwd()
latest_path = os.path.dirname(base_path)
data=read_json_value(key="test",file=None)
print(data)