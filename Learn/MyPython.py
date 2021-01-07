# -*- coding = utf8 -*-
# 单行注释

import keyword
import math
import random

"""
多行注释
"""

'''
多行注释
'''

print(keyword.kwlist)  # 查看关键字

'''
age = input("请输入您的年龄：")  # 定义变量age
print("age =", age)
print(type(age))  # 查看变量age的类型
print(id(age))  # 查看变量age的地址
'''

# 取整数部分
print(int(1.11))

# 将序列的所有元素随机排序
list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print(list1)

# 向上取整
print(math.ceil(18.1))

# 向下取整
print(math.floor(19.9))

# 随机产生一个实数，在[1, 100]范围内
print(random.uniform(1, 100))

a = 123456
print(a % 10)  # 6
print((a // 10) % 10)  # 5
print((a // 100) % 10)  # 4
print((a // 1000) % 10)  # 3
print((a // 10000) % 10)  # 2
print(a // 100000)  # 1
