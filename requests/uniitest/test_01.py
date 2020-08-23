#coding = utf-8
import unittest

class Test_01(unittest.TestCase):

#直接跳过执行case
    @unittest.skip("跳过执行")
    def test_01(self):
        print("this is Test_01 test_01")

#增加判断条件，如果4小于5，则跳过执行，否则依然执行
    @unittest.skipIf(4<5,"跳过执行")
    def test_02(self):
        print("this is Test_01 test_02")


if __name__ == '__main__':
    unittest.main()


