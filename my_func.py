
# 定义3个函数

def is_prime(number):
    if number<0 or number in (0,1):
        return  False

    for ele in range(2,number):

        if number % ele ==0:
            return False

        return True

def add(a,b):
    return a+b

def divide(a,b):
    return a/b