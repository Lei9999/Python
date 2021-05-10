"""
1.打印出所有三位数中的水仙花数
2.输出五位数中回文数的数量
3.从控制台输入一个数，判断是否为质数
4.从控制台输入一个数，分解质因数
5.从控制台输入一个字符串，返回这个字符串中有多个个单词
（ a c bb）= 3
（a cc ddddd adf ）= 4
6.从控制台输入一个字符串，打印出这个字符串中所有数字字符的和
（asdf123asdf123）= 1+2+3+1+2+3
（1kljk123jbiu87）= 1+1+2+3+8+7
"""

'''打印出所有三位数中的水仙花数'''
snum = 100
while snum <= 999:
    num1 = snum
    a = num1 // 100
    b = (num1 - (a * 100)) // 10
    c = (num1 - (a * 100) - (b * 10))
    if num1 == (a ** 3) + (b ** 3) + (c ** 3):
        print(num1)  # 153,370,371,407
        snum += 1
    else:
        snum += 1

'''输出五位数中回文数的数量'''
count = 0
hnum = 10000
while hnum <= 99999:
    num01 = hnum
    a01 = num01 // 10000
    b01 = (num01 - (a01 * 10000)) // 1000
    c01 = (num01 - (a01 * 10000) - (b01 * 1000)) // 100
    d01 = (num01 - (a01 * 10000) - (b01 * 1000) - (c01 * 100)) // 10
    e01 = (num01 - (a01 * 10000) - (b01 * 1000) - (c01 * 100) - (d01 * 10))
    if num01 == (e01 * 10000) + (d01 * 1000) + (c01 * 100) + (b01 * 10) + a01:
        count += 1
        hnum += 1
    else:
        hnum += 1
print("五位数中的回文数共计%d个" % count)  # 五位数中的回文数共计1000个

'''从控制台输入一个数，判断是否为质数'''
znum = int(input("请输入一个大于1的自然数："))
num00 = 2
check = 0
while znum <= 1:
    znum = int(input("您的输入有误，请重新输入一个大于1的自然数："))
while num00 < znum:
    if znum % num00 == 0:
        check += 1
    num00 += 1
if check == 0:
    print("%d是一个质数" % znum)
else:
    print("%d不是一个质数" % znum)

'''
从控制台输入一个数，分解质因数
只有合数才有质因数
质数的质因数是本身
'''
listNum = []
Num = int(input("请输入一个数字："))
count = 2
while count < Num:
    if Num % count == 0:
        Num = int(Num / count)
        listNum.append(count)
        count = 1
    count += 1
listNum.append(Num)
print(listNum)
'''
# 去掉列表中重复的数值
count1 = 1
while count1 <= (len(listNum) - 1):
    if listNum[count1] == listNum[count1 - 1]:
        listNum.pop(count1 - 1)
        count1 = 0
    count1 += 1
print(listNum)
'''

'''
从控制台输入一个字符串，返回这个字符串中有多个个单词
'''
str = input("请输入一串字符：")
str1 = str.strip()
index = 0
count = 0
while index < len(str1):
    while str1[index] != " ":
        index += 1
        if index == len(str1):
            break  # 结束循环
    count += 1
    if index == len(str1):
        break  # 结束循环
    while str1[index] == " ":
        index += 1
print(count)
