"""
什么是字符串
字符串是以单引号或双引号括起来的任意文本
"abc"
'def'
字符串不可变
"""

# 创建字符串
str1 = "Hello, World"
str2 = "World"
str3 = "Hello"

'''
字符串运算
'''
# 字符串连接
str4 = "Hello,"
str5 = "World"
str6 = str4 + str5
print("str6 =", str6)

# 输出重复字符串
str7 = "good"
str8 = str7 * 3
print("str8 =", str8)

# 访问字符串中的某一个字符
# 通过索引下标查找字符，索引从0开始
# 字符串名[下标]
str9 = "Hello World"
print(str9[1])
# str9[1] = "e"
# 字符串不可变
# print("str9 =", str9)

# 截取字符串中的一部分
str10 = "Hello World"
str11 = str10[6:11]  # 从给定下标处开始截取到给定下标之前：6包含，11是之前（不包含）
str12 = str10[:6]  # 从头截取到给定下标之前
str13 = str10[7:]  # 从给定下标处开始截取到结尾
print("str11 =", str11)
print("str12 =", str12)
print("str13 =", str13)

# 判断
# 返回的值 True/False
str14 = "Hello, World"
print("Hello" in str14)
print("Hello1" in str14)
print("Hello1" not in str14)

# 格式化输出（占位符）
print("Hello, World")
# 整数的占位符 %d
num = 10
# 字符串的占位符 %s
str15 = "Hello, World"
# 浮点数的占位符 %f,%.3f：精确到小数点后3位，四舍五入
f = 3.1415926
print("num =", num)
print("num = %d, str15 = %s, f = %.3f" % (num, str15, f))

'''
转义字符：\
将一些字符转换成有特殊含义的字符
\n 换行符，表示一个字符
'''
print("num = %d\nstr15 = %s\nf = %.3f" % (num, str15, f))
# \\
print("Hello \\ World")
# Hello,'W'orld
print('Hello,\'W\'orld')
# Hello,"W"orld
print("Hello,\"W\"orld")
# 如果字符串中有很多换行，用 \n 写在一行不适合阅读
print('''
Hello
World
Hi
Nice
''')
# \t 制表符（默认为4个空格）
print("Hello\tWorld")
'''
如果字符串中有好多字符串需要转义，就需要加入好多斜杠
为了简化，Python允许使用r表示内部的字符串默认不转义
例如：输出Windows下路径 D:\Dism++\Config\amd64
'''
print(r"\\\t\\")
print(r"D:\Dism++\Config\amd64")
print("D:\\Dism++\\Config\\amd64")
print("/root/user/lei/Desktop/temp/")
'''
linux   /root/user/lei/Desktop/temp/
'''
# 方法
# eval(str)
# 将字符串str当成有效的表达式来求值并返回计算结果
print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("12-3"))
# print(eval("a123"))
# print(eval("12a3"))

# len(str)
# 返回字符串的长度
print(len("Hello, World"))

# lower()
# 转换字符串中的大写字母为小写字母
str16 = "Hello, World"
print(str16.lower())

# upper()
# 转换字符串中的小字母为大写字母
print("abc".upper())

# swapcase()
# 转换字符串中的小字母为大写字母,大写字母为小写字母
print("AbCdEfg".swapcase())

# capitalize()
# 首字母大写，其他小写
print("aaaBBBBBddd".capitalize())

# title()
# 每个单词的首字母大写
print("hello worlD".title())

# character    char  字符的意思
# center(width, fillchar)
# 返回一个指定长度的居中的字符串，并使用定义的字符（fillchar）进行填充
# 默认使用空格进行填充
print("Hello, World".center(20, "-"))

# ljust(width[, fillchar])
# 返回一个指定长度的左对齐的字符串，并使用定义的字符（fillchar）进行填充
# 默认使用空格进行填充
print("Hello, World".ljust(40, "*"), "$")


# rjust(width[, fillchar])
# 返回一个指定长度的右对齐的字符串，并使用定义的字符（fillchar）进行填充
# 默认使用空格进行填充
print("Hello, World".rjust(40, "*"))

# zfill(width)
# 返回一个指定长度的右对齐的字符串，并使用"0"进行填充
print("Hello, World".zfill(40))

# count(str[, start][, end])
# 返回字符串中str出现的次数，可以指定一个范围，默认从头到位
str17 = "I'm a good good man"
print(str17.count("good", 4, len(str17)))  # 从4开始查找，到该字符串的末尾结束

# find(str[, start][, end])
# 从左至右查找str字符串是否包含在调用的字符串中，可以指定范围，默认从头到位
# 得到的是第一次出现的下标
# 若未检测到则返回值为 -1
str18 = "I'm a good good man"
print(str18.find("good"))

# rfind(str[, start][, end])
# 从右至左检测str字符串是否包含在调用的字符串中，可以指定范围，默认从头到位
# 得到的是第一次出现的下标
# 若未检测到则返回值为 -1
str19 = "I'm a good good man"
print(str19.rfind("good", 0, 10))

# index(str, start=0, end=len(str))
# 与find方法一样
# 若str不存在时返回一个异常
str20 = "I'm a good good man"
print(str20.index("good"))

# rindex(str, start=0, end=len(str))
# 与rfind方法类似
# 若str不存在时返回一个异常

# lstrip()
# 截取掉字符串左侧指定的字符，默认为空格
str21 = "    Hello, World！"
print(str21.lstrip())
str22 = "-----Hello, World！"
print(str22.lstrip("-"))

# rstrip()
# 截取掉字符串右侧指定的字符，默认为空格

# strip()
# 截取掉字符串左右两侧指定的字符，默认为空格
str23 = "**********Hello, World！**********"
print(str23.strip("*"))

# ASCII码换算
str24 = "a"
print(ord(str24))  # 将字符串"a"转换为ASCII码
str25 = chr(65)
print(str25)  # 将ASCII码"65"转换为字符串

# 字符串比较大小
# 从第一个字符开始比较，谁的ASCII值大谁就大，
# 如果相同，则比较下一个字符的ASCII值
# 较短字符串中，使用“|0”补位
print("a" > "b")  # False
print("Good" == "Good" )  # True
print("baaaa" < "azzzz")  # False
print("azzzz" < "m")  # True
print("mszzz" < "ms")  # False,"|0"代替空

'''
将字符串切割为list
'''
# split(str='', number)
# 以str为分隔符截取字符串,若指定number,则仅截取number个字符串
# 剩下的放在一起
str26 = 'shilei*is****a**good*man'
print(str26.split('*', 3))
# ['shilei', 'is', '', '**a**good*man']
list26 = str26.split('*')
c = 0
for s in list26:
	if len(s) > 0:
		c += 1
print(c)  # 求字符串中单词的个数

# splitlines([keepends])
# keepends == True 保留换行符
# 按照(\r | \n | \r\n)分隔
str27 = '''shilei is a good man!
shilei is a nice man!
shilei is an superman!
'''
print(str27.splitlines())
print(str27.splitlines(True))

'''
组合
'''
# "str".join(seq)
# 以指定的字符串分隔符(str),将seq中的所有元素组合成一个字符串
list27 = ['shilei', 'is', 'good', 'man']
str28 = '*'.join(list27)
print(str28)

# max()
# min()
str29 = 'shilei is a good man!z'
print(max(str29))
print('*'+min(str29)+'*')  # 打印出空格

# str.replace(oldstr, newstr, count)
# 用'newstr'替换'oldstr',默认全部替换
# 如果指定count,那么只替换count个
str30 = 'shilei is a good good good man!'
str31 = str30.replace('good', 'nice', 1)
print(str30)
print(str31)

# 创建一个字符串映射表
t32 = str.maketrans('ac', '65')
# a--6	c--5
str32 = 'shilei is a good man!'
str33 = str32.translate(t32)
print(str33)

# startwith(str, start=(), end=len(str))
# 在给定的范围内判断是否以给定的字符串开头
# 如有没有指定范围，默认整个字符串
str34 = "shilei is a good man"
print(str34.startswith("shi", 5, 16))  # False

# endswith(str, start=0, end=len(str))
# 在给定的范围内判断是否以给定的字符串结果
# 如果没有指定范围，默认整个字符串
str35 = "Shilei is a nice man"
print(str35.endswith("man"))

# 编码
# encode(encoding="utf-8", errors="strict")
str36 = "shilei is a good man 磊"
# ignore 忽略错误
data26 = str36.encode("utf-8", "ignore")
print(data26)
print(data26)  # <class 'bytes'>

# 解码
# decode
# 注意：要与编码时的编码格式一致
str37 = data26.decode("utf-8", "ignore")
str38 = data26.decode("gbk", "ignore")
print(str37)  # shilei is a good man 磊
print(str38)  # shilei is a good man 纾

# isalpha()
# 如果字符串中至少有一个字符且所有的字符都是字母返回True，否则返回False
str39 = "shilei is a good man"
str40 = "abcdefg"
print(str39.isalpha())  # False
print(str40.isalpha())  # True

# isalnum()
# 如果字符串中至少有一个字符且所有的字符都是字母或数字返回True，否则返回False
str41 = "123"
str42 = "1qwe123"
print(str41.isalnum())  # True
print(str42.isalnum())  # True

# isupper()
# 如果字符串中至少有一个英文字符且所有的英文字符都是大写的英文字母，返回True，否则返回Flase
print("ABC".isupper())  # True
print("ABC1d".isupper())  # False
print("1".isupper())  # False
print("ABC1".isupper())  # True
print("ABC#".isupper())  # True

# islower()
# 如果字符串中至少有一个英文字符且所有的英文字符都是小写的英文字母，返回True，否则返回Flase
# 与isupper()对应

# istitle()
# 如果字符串是标题化的返回True，否则返回False
print("shilei".istitle())  # False
print("Shilei is".istitle())  # False
print("Shilei Is".istitle())  # True

# isdigit()
# 如果字符串只包含数字字符，返回True，否则返回False
print("123".isdigit())  # True

# isnumeric()
# 同'isdigit()'
print("123".isnumeric())

# isdeciaml()
# 字符串只包含10进制字符，返回True，否则返回False
print("123".isdecimal())

# isspace()
# 字符串只包含空格，返回True，否则返回False
# 一下均为True
print(" ".isspace())
print("   ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())



