"""
for语句

格式：
for 变量名 in 集合:
    语句

逻辑：
按顺序取“集合”中的每个元素赋值给“变量”，再去执行语句
如此循环，直至取完“集合”中的元素
"""

for i in [1, 2, 3, 4, 5]:
    print(i)  # 打印1 - 5

'''
range([start,] end[, step])函数   “列表生成器”
start = 0（默认）
step = 1（默认）
功能：生成数列
'''

a = range(10)
print(a)
for x in range(10):
    print(x)
for y in range(2, 10, 2):  # 2起点，10终点，2步长
    print(y)

# 同时便利下标和元素
for index, m in enumerate([1, 2, 3, 4, 5]):  # index, m = 下标, 元素
    print(index, m)

# 1加到100
sum = 0
for n in range(1, 101):
    sum += n
print(sum)
