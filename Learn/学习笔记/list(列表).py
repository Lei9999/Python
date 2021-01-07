# 存储5个人的年龄，求他们的平均年龄
age1 = 18
age2 = 19
age3 = 20
age4 = 21
age5 = 22
print((age1 + age2 + age3 + age4 + age5) / 5)

# 使用列表功能实现求平均年龄
list5 = [18, 19, 20, 21, 22]
index = 0
sum0 = 0
# 嵌套最好不要超过3层
while index < 5:
    sum0 += list5[index]
    index += 1
    if index == 5:
        print("平均年龄：%d" % (sum0 / 5))

'''
思考：若要存储100个人的年龄？
解决：使用列表（数据类型）
本质：是一种有序的集合
'''
'''
创建列表
格式：列表名 = [列表选项1, 列表选项2, 列表选项3, ……, 列表选项n]
注意：列表中的元素类型可以是多种类型
'''
# 创建了一个空列表
list1 = []
print(list1)

# 创建带有元素的列表
list2 = [18, 19, 20, 21, 22]  # 列表中的类型为数字
list3 = [1, 2, "Abc", "good", True]  # 列表中的元素类型为多种类型
print(list3)

'''
列表元素的访问
注意：不要越界（下标超出可表示的范围）
取值
格式：列表名[下标]  # 下标从0开始

替换
'''
# 取值
list4 = [1, 2, 3, 4]
print(list4[2])  # 取值3
# 替换
list4[2] = 100  # 3替换为100
print(list4[2])

'''
列表操作
'''
# 列表组合
list6 = [1, 2, 3]
list7 = [4, 5, 6]
list8 = list6 + list7
print(list8)

# 列表的重复
list9 = [1, 2, 3]
print(list9 * 3)

# 判断元素是否在列表中
list10 = [1, 2, 3, 4]
print(3 in list10)
print(6 in list10)

# 列表的截取
list11 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list11[2:5])
print(list11[2:])
print(list11[:5])

# 二维列表
# 元素也是一个列表
list12 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list12[1])  # [4, 5, 6]
print(list12[1][1])  # 5

# 列表方法
# append 在列表的末尾添加新的元素
list13 = [1, 2, 3, 4, 5]
print(list13)
list13.append(6)
print(list13)
list13.append([6, 7, 8])

# extend 在末尾一次性追加另一个列表中的多个值
list14 = [1, 2, 3]
list14.extend([4, 5, 6])
print(list14)

# insert 在下标处添加一个元素，不覆盖原数据，原数据向后顺延
list15 = [1, 2, 3, 4, 5]
list15.insert(0, 100)
print(list15)
list15.insert(2, [1, 2])  # [1, 2]当成一个元素来处理
print(list15)

# pop(x=list[-1])
# 移除列表中指定下标处的元素（默认移除最后一个元素），并返回删除的数据
list16 = [1, 2, 3, 4, 5]
print(list16[-1])  # 5 代表最后一个下标
list16.pop()
print(list16.pop())
print(list16)
list16.pop(0)
print(list16)

# remove 移除列表中的某个特定元素，只移除第一个匹配的结果（从左至右）
list17 = [1, 2, 3, 4, 5, 4]
list17.remove(4)
print(list17)

# clear 清除列表中所有的数据
list18 = [1, 2, 3, 4, 5, 4]
list18.clear()
print(list18)

# 从列表中找到某个值，列出第一个匹配的索引值的下标
list19 = [1, 2, 3, 4, 5, 4]
index18 = list19.index(4)
index19 = list19.index(4, 4, 6)  # 圈定一个范围，6代表是6之前不包含6（一共5个）
print(index18, index19)  # 3，5

# 列表中元素个数
list20 = [1, 2, 3, 4, 5, 6, "a"]
print(len(list20))  # 7

# 获取列表中最大值
list21 = [1, 2, 3, 4, 5, 6, "a"]
print(max(list21))  # 不成立，int 无法与 str 比较大小
list21 = ["a", "b"]
print(max(list21))  # b 最大
list21 = [1, 2, 3, 4, 5, 6]
print(max(list21))  # 6 最大

# 获取列表中最小值
list22 = [1, 2, 3, 4, 5, 6]
print(min(list22))  # 1 最小

# 查看元素在列表中出现的次数
list23 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(list23.count(3))

# 倒序
list24 = [1, 2, 3, 4, 5, 6]
list24.reverse()
print(list24)

# 排序 升序
list25 = [1, 3, 5, 4, 2, 6]
list25.sort()
print(list25)

# 拷贝
# 浅拷贝 引用拷贝
list26 = [1, 3, 5, 4, 2, 6]
list27 = list26
list27[1] = 200
print(list27)  # [1, 200, 5, 4, 2, 6]
print(list26)  # [1, 200, 5, 4, 2, 6]
print(id(list27))  # 4088392
print(id(list26))  # 4088392
# 深拷贝 内存的拷贝
list28 = [1, 3, 5, 4, 2, 6]
list29 = list28.copy()
list29[1] = 100
print(list28)
print(list29)

# 将元素转成列表
list30 = list((1, 2, 3, 4))  # list() 元祖
print(list30)  # []，列表

'''
找出第二大的值
'''
# 方法1
listNum = []
num = 0
while num < 5:
    val = int(input("请输入数值："))
    listNum.append(val)
    num += 1
print(listNum)
listNum.sort()  # 将列表排序
count = listNum.count(listNum[len(listNum) - 1])  # 得到最大值出现的次数
c = 0
while c < count:  # 删除最大值
    listNum.pop()
    c += 1
print(listNum[len(listNum) - 1])  # 最后一个便是原来整个列表的第二大值



