

# 1.计算从1到1000以内所有能同时被3，5和7整除的数的和并输出
sum1 = 0
for i in range(1, 1000+1):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        sum1 += i
print(sum1)

# 2.有四个数字，1，2，3，4能组成多少个互不相同且无重复的三位数？各是多少？
a = [1,2,3,4]
count = 0
for i in a:
    for j in a:
        for k in a:
            if i != j and i != k and j != k:
                count += 1
                print(i * 100 + j * 10 + k)
print("一共:"+str(count))

# 3.有一个棋盘，有64个方格，在第一个方格里面放1粒芝麻重量是0.00001kg，
#   第二个里面放2粒，第三个里面放4，... 求棋盘上放的所有芝麻的重量
height2 = 0.00001
sum1 = 0
for i in range(1, 65):
    sum1 += 2 ** (i-1)
print(sum1 * height2)
#方法二：
height2 = 0.00001
sum1 = 0
for i in range(64):
    sum1 += 2 ** i
print(sum1 * height2)


# 3.小明入职月薪是10000，每年涨当年月薪的10%, 问50年后小明的月薪是多少
sum1 = 10000
sum2 = 0
for i in range(1, 51):
    sum1 *= 1+0.1
print(sum1)
#方法二:
sum1 = 10000
sum2 = 0
for i in range(50):
    sum1 *= 1+0.1
print(sum1)

# 4.不停输入一个骰子的编号(1-6)根据骰子点数决定什么惩罚
#  【1.跳舞，2.唱歌,3.真心话,4.大冒险,5.喝酒.6.退出break】
while True:
    a = int(input())
    if a == 1:
        print("跳舞")
    elif a == 2:
        print("唱歌")
    elif a == 3:
        print("真心话")
    elif a == 4:
        print("大冒险")
    elif a == 5:
        print("喝酒")
    else:
        break

# 5.求1000以内的水仙花数.（水仙花数：一个三位数各个位上的立方之和，等于本身。）
# 例如： 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
print("============")
for i in range(100, 1000):
    a , b, c = i // 100 % 10, i // 10 % 10, i // 1 % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(a, b, c, "===", i)

print("==============")
# 挑战题
#
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下。求它在第n次落地时，共经过多少米？(难度： * * * *)
# 规律:
#     第1次落地: 100
#     第2次落地: 100 + 50x2
#     第3次落地: 100 + 50x2 + 25x2
#     第4次落地: 100 + 50x2 + 25x2 + 12.5x2
#     第5次落地: 100 + 50x2 + 25x2 + 12.5x2 + ...
#                     50     25      12.5     6.25 ...

n = int(input("请输入第几次落地:"))
sum1 = 0
height = 100
for i in range(1, n + 1):
    sum2 = height/i
    if i != 1:
        sum1 += sum2 * 2
    else:
        sum1 += sum2
print(sum1)
#方法二
s = 100
for i in range(1, n):
    s += 100/(2 ** i) * 2
print(s)