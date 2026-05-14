
# 作业

# 已知列表 names = ['jeff','rain','jack','lucy','lance','feifei']
# a.往names列表里feifei前面插入一个alex
names = ['jeff','rain','jack','lucy','lance','feifei']
a = names.index('feifei')
names.insert(a,'alex')
print(names)
# b.把lucy的名字改成中文：路西
names = ['jeff','rain','jack','lucy','lance','feifei']
a = names.index('lucy')
names[a] = '路西'
print(names)
# c.往names列表里rain的后面插入一个子列表，[oldboy, oldgirl]
b = ['oldboy', 'oldgirl']
names = ['jeff','rain','jack','lucy','lance','feifei']
a = names.index('rain')
print(names[0, a] + b + names[a:])
# d.返回lance的索引值
names = ['jeff','rain','jack','lucy','lance','feifei']
print(names.index('lance'))
# e.创建新列表["佩奇", "喜羊羊"],合并入names列表
b = ["佩奇", "喜羊羊"]
names = ['jeff','rain','jack','lucy','lance','feifei']
print(names.extend(b))
# f.取出names列表中索引4-7的4个元素
names = ['jeff','rain','jack','lucy','lance','feifei']
print(names[4:8])
# g.取出names列表中索引2-10的5个元素，步长为2
print(names[2:11:2])
# h.取出names列表中最后3个元素
print(names[-1:-4])
# I.循环names列表，打印每个元素和索引值，如果索引值为偶数时，把对应的元素改成-1

for k,v in enumerate(names):
    if k %2 == 0:
        names[k] = 0

print(names)