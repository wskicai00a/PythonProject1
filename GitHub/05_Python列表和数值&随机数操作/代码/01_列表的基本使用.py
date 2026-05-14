
# Python数据类型:
#  int, float, str, bool, NoneType,
#  list, tuple, dict, set(了解), bytes
#   列表, 元表    字典   ???

# list列表 : Array数组
# 为什么要使用列表：
# 举例：如果我们表示汽车品牌用变量保存单个值
a = "BYD"
b = "五菱宏光"
c = "小米"
d = "蔚来"
e = "法拉利"
f = "兰博基尼"
g = "路虎"
# 如果要你表示300个品牌, 变量就太多了，这时我们可以使用列表来表示：
cars = ["BYD", "五菱宏光", "小米", "蔚来", "蔚来", "法拉利", "兰博基尼", "路虎"]



# 列表的基本功能
# 1.列表定义
nums = [1, 2, 3, 4, 5]

# 2.索引,下标
#   从0开始
print("第一个元素：", nums[0])
print("倒数第一个元素：", nums[-1])

# 3.长度,元素个数
print("列表长度：", len(nums))

# 4.遍历,循环
for i in nums:
    print(i)
for i in range(len(nums)):
    print(i, "===", nums[i])
for i,v in enumerate(nums):
    print(i, "===", v)
# 5.修改列表
nums[0] = 666#将第一个元素修改为666

# 6.切片 (很重要) : 不会修改原列表
#    list[start : stop : step] : [start, stop)
#  和range(start, stop, step)类似  [start, stop)
ages = [10,20,30,40,50,60,70,90]
print(ages[:])#取列表的全部数据
print(ages[0:5])#取列表索引为0-4的数据
print(ages[:5])#取列表索引为0-4的数据
print(ages[5:])#取列表索>=5的数据
print(ages[0:5:2])#取列表索引为0-4的数据,步长为2
print(ages[5:0:-1])#取列表索引为0-4的数据,倒序
print(ages[::-1])#取列表所有的数据,倒序



# 7. 合并 +  (了解)

a=[1,2,3]
b=[3,4,5]
print(a + b)#合并列表a和b
# 8. 重复 * (了解)
print(a * 3)#将a重复三次，然后合并成一个列表

# 9. 成员 in (掌握)


# 需求: 列表去重 (掌握)
nums=[1,2,3,1,2,3]
nums2=[]
for n in nums:
    if n not in nums2:
        nums2.append(n)
print(nums2)

# 10.删除元素 del (了解)

del nums2[0]
del nums2[:2]
