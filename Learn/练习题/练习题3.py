"""
1.打印99乘法表
2.输入两个数，求这两个数的最大公约数
3.输入一个字符串，将字符串中的大写字母转为小写，将小写字母转为大写（不允许使用。。）
4.随机生成一个6位数的验证码（包含：大写字母，小写字母，数字）
"""

# 打印99乘法表
for y in range(1, 10):
    for x in range(1, 10):
        print('{0}x{1}={2}'.format(y, x, (x * y)), end=" ")
        if x == y:
            break
    print()
    y += 1

# 输入两个数，求这两个数的最大公约数
listx = []
listy = []
Numx = int(input("请输入第一个数字："))
Numy = int(input("请输入第二个数字："))
# 计算第一个数的质因数
countx = 2
while countx < Numx:
    if Numx % countx == 0:
        Numx = int(Numx / countx)
        listx.append(countx)
        countx = 1
    countx += 1
listx.append(Numx)
print("第一个数的质因数为：{0}".format(listx))
'''
# 去除第一个数的质因数中的重复数值
countx1 = 1
while countx1 <= (len(listx) - 1):
    if listx[countx1] == listx[countx1 - 1]:
        listx.pop(countx1 - 1)
        countx1 = 0
    countx1 += 1
print("第一个数的质因数去重后：{0}".format(listx))
'''
# 计算第二个数的质因数
county = 2
while county < Numy:
    if Numy % county == 0:
        Numy = int(Numy / county)
        listy.append(county)
        county = 1
    county += 1
listy.append(Numy)
print("第二个数的质因数为：{0}".format(listy))
'''
# 去除第二个数的质因数中的重复数值
county1 = 1
while county1 <= (len(listy) - 1):
    if listy[county1] == listy[county1 - 1]:
        listy.pop(county1 - 1)
        county1 = 0
    county1 += 1
print("第二个数的质因数去重后：{0}".format(listy))
'''
# 将两个列表中的数值合并，并去重
listNum = listx + listy
listNum.sort()  # 将列表排序
# 将合并后的列表去重
count1 = 1
while count1 <= (len(listNum) - 1):
    if listNum[count1] == listNum[count1 - 1]:
        listNum.pop(count1 - 1)
        count1 = 0
    count1 += 1
print(listNum)
'''
listNum = []
for x in listx:
    if x in listy:
        listNum.append(x)
    else:
        listNum.append(x)
for y in listy:
    if y in listx:
        print()
    else:
        listNum.append(y)
print(listNum)
'''
product = 1
for n in listNum:
    product *= n
print("这两个数的公约数为：{0}".format(product))
