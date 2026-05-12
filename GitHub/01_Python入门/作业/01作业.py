
'''
1. 写一个初级程序：先输入自己的名字，如输入：张三，则打印"大家好，我是 张三"
'''
import math

name = input("你的名字是：")
print(name)


'''
2. 分隔符输出字符串：
在控制台分别输入3个变量a,b,c，然后用print输出这3个变量组成的字符串，中间要求使用分隔符加号（+）连接, 要求使用sep
例如：输入3个字符串“Python”、“is”、“Wonderful”，结果显示为“Python+is+Wonderful”
'''
a = input("变量1：")
b = input("变量2：")
c = input("变量3：")
print(a, b, c, sep="+")



'''
3.使用input在控制台输入半径r，求面积S 和  周长C,   π=3.14
   公式： 面积S = 半径r * 半径r * 3.14
		 周长C = 半径r * 3.14 * 2
'''
PI = 3.14
r = input("请输入半径：")
print("面积是：", PI * int(r)**2)
print("面积是：", PI * math.pow(int(r), 2))
print("周长是：", PI * int(r)*2)