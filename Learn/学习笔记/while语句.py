"""
while 语句：

格式：
while 表达式:
    语句

逻辑：
当程序执行到“while语句”时，首先计算“表达式”的值
    如果“表达式”的值为假，那么结束整个“while语句”
    如果“表达式”的值为真，则执行“while语句”
执行完“while语句”，再去计算“表达式”的值
如此循环，直到“表达式”的值为假
"""

# 打印从1到5
num0 = 1
while num0 <= 5:
    print(num0)
    num0 += 1

# 打印机从1加到100的和（1+2+3+...+100）
sum1 = 0
num1 = 1
while num1 <= 100:
    sum1 += num1  # 1+...+99+100
    num1 += 1  # num1 = num1 + 1
print("sum = %d" % sum1)

# 打印字符串中每一个字符
str0 = "Hello, World!"
index = 0
while index < len(str0):  # len(str) 返回字符串的长度，从1开始，所以此处需要用"<"即可
    print("str[%d] = %s" % (index, str0[index]))  # str[index] 访问字符串中的某一个字符,通过索引下标查找字符，索引从0开始
    index += 1  # (index = 12) == (len(str) = 13)

"""
死循环：
表达式永远为真的循环
"""

while 1:
    print("死循环了！我停不下来了！")






