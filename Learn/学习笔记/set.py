'''
set：类似dict，是一组key的集合，不存储values

本质：无序、无重复元素的集合
'''
# 创建
# 创建set需要一个list或者tuple或者dict作为输入
# 重复元素在set中会自动过滤
set_ex1 = set([1, 2, 3, 4, 5, 4, 5])
print(set_ex1)

set_ex2 = set((1, 2, 3, 4, 5, 4, 5,))
print(set_ex2)

set_ex3 = set({1:"good", 2:"nice"})
print(set_ex3)  # 只打印key

# 添加
# 可以添加重复的，但是无效果
set_ex4 = set([1, 2, 3, 4, 5])
set_ex4.add(6)
set_ex4.add(3)  # 无效果
# set_ex4.add([7, 8, 9])  # 报错，list可变，不能作为key
set_ex4.add((7, 8, 9))  # 可行，元祖不可变
# set_ex4.add({1:"a"})  # set的元素不能是字典，因为字典可变
print(set_ex4)

# 插入整个list，tuple，字符串（打碎插入）
set_ex5 = set([1, 2, 3, 4, 5])
set_ex5.update([6, 7, 8])
set_ex5.update((9, 10))
set_ex5.update("abcd")  # 'a', 'b', 'c', 'd'
print(set_ex5)

# 删除
set_ex6 = set([1, 2, 3, 4, 5])
set_ex6.remove(3)  # 删除3，无法根据下标删除，因为无序，没有下标
print(set_ex6)

# 遍历
set_ex7 = set([1, 2, 3, 4, 5])
for i in set_ex7:
    print(i)
# 无索引

for index, data in enumerate(set_ex7):
    print(index, data)

set_ex8 = set([1, 2, 3])
set_ex9 = set([2, 3, 4])
# 交集
a1 = set_ex8 & set_ex9
print(a1)
print(type(a1))
# 并集
a2 = set_ex8 | set_ex9
print(a2)
print(type(a2))


