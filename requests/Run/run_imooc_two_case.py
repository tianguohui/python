#coding = utf-8
from Excel_case.excel_def_case import Handexcel
from Base_request.base_request import request
from Run.read_json import *
import json
import unittest
json_file_name = "/Config/result_imooc.json"

class RunMain(unittest.TestCase):
    def test_run_main(self):
        max_rows = Handexcel.get_row_max()
        for row in range(max_rows):
            data = Handexcel.get_row_value(row+2)
            data_method = data[4]
            data_url = data[3]
            data_data = data[5]
            is_run = data[2]
            if is_run == 'yes':
                result_data_json = read_json_value(file=json_file_name,key=data_url)
                #print(result_data_json)
                for list in result_data_json:
                    if list['result'] != None:
                        result_data = list['result']
                    if list['msg'] !=None:
                        msg_data = list['msg']
                res = request.send_main(data_method,data_url,data_data)
                self.assertEqual(res['result'],result_data)
                self.assertEqual(res['msg'],msg_data)

               # print(res)
            else:
                pass

if __name__ == '__main__':
    unittest.main()
