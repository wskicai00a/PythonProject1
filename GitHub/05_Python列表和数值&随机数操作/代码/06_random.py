
# random: 随机数

# import keyword
# import math
# import time
import random

from tornado.gen import sleep

# random.choice(): 从列表/str中随机取一个元素
# random.randint(a, b): 从一个范围随机取一个整数，闭区间
# random.randrange(a, b, step): 随机获取一个奇数，和range类似
# random.random() : 在0~1之间[0,1)随机获取一个小数

# random.uniform(3, 5) ： 3~5之间的小数 （了解）
# random.shuffle(list) : 随机打乱顺序  （了解）

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b="abcdefghijklmnopqrstuvwxyz"
print(random.choice(a))#从列表/str中随机取一个元素
print(random.choice(b))#从列表/str中随机取一个元素
print(random.randint(1, 10))#从一个范围随机取一个整数，闭区间
print(random.randrange(10))#随机获取一个奇数，和range类似
print(random.randrange(2, 10, 2))#随机获取一个奇数，和range类似
print(random.random())#在0~1之间[0,1)随机获取一个小数

print("=========")
while True:
    sleep(0.1)
    a = random.random()
    if a == 0:
        print('000000')
    elif a == 1:
        print('111111')