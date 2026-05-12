
# if分支结构

# Python语言有强制缩进


# 单分支


# 双分支


# 多分支
#  age范围
#    age<18 : 未成年
#    18~30 : 年轻人
#    30~60 : 中年人
#    age>60 : 老年人





# 练习：
#    输入年龄age，要求输入0~12岁之间
#    0~3 : 婴儿
#    3~6 ： 幼儿
#    6~12 ：儿童

age = 10
if 0<=age<3:
    print("婴儿")
elif 3<=age<6:
    print("幼儿")
else:
    print("儿童")

# 练习2：
#    输入性别sex,判断sex
#    如果sex=='男'：输出王思聪
#    如果sex=='女'：输出刘亦菲
#    否则：输出泰国人

sex = '男'
if sex == "男":
    print("王思聪")
elif sex == '女':
    print("刘亦菲")
else:
    print("泰国人")


# if嵌套
#   可以在if语句中 再写if
# 比如：有一个女孩，她母亲要给他介绍对象，女孩有几个要求：
#   1.年龄<=30
#   2.身高>=1.75m
#   3.年薪>=20w

age = 30
height = 175
money=20
if age <= 30:
    if height >= 175:
        if money >= 20:
            print("这是如意郎君")
print('end')

# if 条件
# bool值隐式判断




# 扩展
# 输入2个数，得到较大的数
a = 10
b = 12
print(a > b and a or b, "===aaa")


# 练习：
#   input("请说出你的心里话(喜欢/不喜欢):")
#   如果喜欢，输出：小女子无以为报,只有以身相许
#   如果不喜欢，输出：小女子无以为报,只有来世做牛做马报答公子大恩
a = "喜欢"
print(a == "喜欢" and "小女子无以为报,只有以身相许" or "小女子无以为报,只有来世做牛做马报答公子大恩")


# 练习：
# 输入一个成绩score,判断这个成绩属于哪个等级
#    score >= 90: A
#    70<= score <90: B
#    60<= score <70: C
#    score < 60 : D

score = 100
if score >= 90:
    print("A")
elif 90 > score >= 70:
    print("B")
elif 70 > score >= 60:
    print("C")
else:
    print("D")
