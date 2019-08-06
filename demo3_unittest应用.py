import unittest
from my_func import *

#定义测试方法，需要继承uittest.TestCase类
class TestMyfunc(unittest.TestCase):

    # 1
    def setUp(self):
        print("每个用例执行之前会调用setUp方法")


    #2  测试用例以test开头
    def test_is_preme(self):
        print("is_prime")
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(8))


    # 3
    def tearDown(self):
        print("每个用例执行完成后会调用teardown方法进行环境清理")

    def test_add(self):
        print("add")
        self.assertEqual(3,add(1,3))

    def test_divide(self):
        print("divide")
        self.assertEqual(2,divide(6,3))
        self.assertNotEqual(2,divide(5,2))

if __name__ == '__main__':
    unittest.main()