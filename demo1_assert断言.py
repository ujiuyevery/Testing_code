'''
assert 断言语句 和if分支语句 有点类似，它用于对一个bool 表达式进行断言
如果为true 继续向下执行，否则执行中断
if 条件:
    执行1
else:
    执行2

'''
s_age = input("请输入年龄:")
age = int(s_age)

assert  20<age<80

print("您输入的年龄在20-80之间")

'''
assert 如果表达式不成立会引入AssertionError
assert True  正常
assert Flase  报错

'''