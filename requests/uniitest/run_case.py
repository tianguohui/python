#coding = utf-8
import unittest
import os

'''
#导入uniitest文件夹中的类class，语法：from 文件夹.文件名称 import class类名称
from uniitest.test_01 import Test_01
from uniitest.test_02 import Test_02

#定义集合：case_01,case_02
case_01 = unittest.TestLoader().loadTestsFromTestCase(Test_01)
case_02 = unittest.TestLoader().loadTestsFromTestCase(Test_02)

#执行suite套件运行程序
suite = unittest.TestSuite([case_01,case_02])
unittest.TextTestRunner().run(suite)
'''

'''
1、获取当前文件夹目录
2、使用discover函数，设置需要运行的文件，通过正则表达式，运行test开头的文件
3、运行suite套件
'''
case_path = os.getcwd()
print(case_path)
discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
unittest.TextTestRunner().run(discover)



