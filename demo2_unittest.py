import unittest

#使用方法

class OurTest(unittest.TestCase):

    '''继承编写测试的基础类'''

    def setUp(self):
        #类似于init方法，在测试执行初自动执行，通常用来做测试准备数据的
        self.a = 1 #测试使用的参数表1
        self.b = 1  # 测试使用的参数2
        self.result = 3  # 预期结果

    def test_add(self):

        """
        j具体测试方法，使用TestCase编写具体测试方法，函数名必须是test开头
        函数当中的内容同常是获取预期值，和结果值进行断言
        """
        run_result = self.a+self.b

        self.assertEqual(run_result,self.result,"self.a+self.b不等于3") #断言两个值是否相等

    def tearDown(self):
        #类似于del方法，用来回收测试环境 ，执行了setUp方法，不论测试是否成功，都执行此方法
        print("tearDown执行---------")

if __name__ == '__main__':
    unittest.main()