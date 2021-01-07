"""
break语句
作用：
跳出for和while的循环
注意：只能跳出距离它最近的那一层循环
"""
# 只打印到5
for i in range(10):
    print(i)
    if i == 5:  # 结束循环
        break

num = 1
while num <= 10:
    print(num)
    if num == 5:
        break
    num += 1
# 注意：循环语句可以有else语句，break导致循环截止，不会执行else语句
else:
    print("不会打印出来！")