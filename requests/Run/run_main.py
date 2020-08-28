#coding = utf-8
from Excel_case.excel_def_case import Handexcel
from Base_request.base_request import request
import os

class RunMain:
    def run_main(self):
        max_rows = Handexcel.get_row_max()
        for row in range(max_rows):
            data = Handexcel.get_row_value(row+2)
            data_method = data[4]
            data_url = data[3]
            data_data = data[5]
            is_run = data[2]
            if is_run == 'yes':
                request.send_main(data_method,data_url,data_data)
            else:
                pass

if __name__ == '__main__':
    run = RunMain()
    run.run_main()
