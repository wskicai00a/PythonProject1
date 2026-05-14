

# 1. 已知列表list1 = ['mon','sun','sat','fri','thu','wed'],
#          list2 = ['sun','wed','thu']，将属于list2的元素从list1中删除
list1 = ['mon','sun','sat','fri','thu','wed']
list2 = ['sun', 'wed', 'thu']
list3 = []
for i, v in enumerate(list1):
    if v not in list2:
       list3.append(v)

print(list3)

# 2. 已知一个列表names = ['鲁班七号', '后裔', '狄仁杰', '黄忠', '孙尚香']，
#    利用索引的方法获取names中的元素黄忠
names = ['鲁班七号', '后裔', '狄仁杰', '黄忠', '孙尚香']
a = '黄忠'
for i, v in enumerate(names):
    if a == v:
        print(names[i])


# 3. 已知一个数字列表nums = [1, 2, 3, 1, 4, 2, 1, 3, 7, 3, 3]，输出索引为奇数的元素
nums = [1, 2, 3, 1, 4, 2, 1, 3, 7, 3, 3]

print(nums[1::2])

