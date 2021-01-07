"""
while 表达式:
    语句1
else:
    语句2

逻辑：
在条件语句（表达式）为False时，执行else中“语句2”
"""

a = 1
while a <= 3:
    print("循环！")
    a += 1
else:
    print("循环结束啦！")
print("退出循环！")
