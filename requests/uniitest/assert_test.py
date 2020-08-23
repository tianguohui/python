import unittest
class UnittestTest(unittest.TestCase):
    def test01_Equal(self):
        a = 'test'
        b = 'test'
        self.assertEqual(a,b)
        print("--> 判断a=b，等于则pass，否则fail")

    def test02_NotEqual(self):
        a = 'test'
        b = 'test1'
        self.assertNotEqual(a,b)
        print("--> 判断a!=b，等于则pass，否则fail")

    def test03_True(self):
        a = True
        self.assertTrue(a)
        print("--> 判断a是否为true，等于则pass，否则fail")

    def test04_False(self):
        a = False
        self.assertFalse(a)
        print("--> 判断a是否为false，等于则pass，否则fail")

    def test05_In(self):
        a = '12'
        b = '1342123456'
        self.assertIn(a,b)
        print("--> （字符串，包含）判断a的内容是否在b中可以找到，等于则pass，否则fail")

    def test06_NotIn(self):
        a = '162'
        b = '1342123456'
        self.assertNotIn(a,b)
        print("--> （字符串，不包含）判断a的内容在b中不能找到，等于则pass，否则fail")

    def test07_DictEqual(self):
        a = {
            "username": 'username'
        }
        b = {
            "username": 'username'
        }
        self.assertDictEqual(a, b)
        print("--> (字典)判断a = b，等于则pass，否则fail")

    def test08_Is(self):
        a = '162'
        b = '162'
        self.assertIs(a,b)
        print("--> a是b，等于则pass，否则fail")

    def test09_IsNot(self):
        a = '162'
        b = '1624'
        self.assertIsNot(a,b)
        print("--> a不是b，等于则pass，否则fail")


if __name__ == '__main__':
    unittest.main()
