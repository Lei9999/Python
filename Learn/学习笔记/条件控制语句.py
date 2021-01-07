"""
if语句

if-else语句

if-elif-else语句
"""
'''
if-elif-else语句
格式：
if      表达式1:
        语句1
elif    表达式2:
        语句2
elif    表达式3:
        语句3
......
elif    表达式n:
        语句n
else:  # 可有可无
        语句
        
逻辑：
当程序执行到if-elif-else语句时，首先计算“表达式1”的值，
如果“表达式1”的值为真，则执行“语句1”，并跳过整个if-elif-else语句
如果“表达式1”的值为假，则执行下一个elif中“表达式2”的值......
如果没有真的表达式且有else语句，则执行else语句
'''

age = int(input("请输入年龄："))
if age < 0:
    print("未出生")
if 0 <= age and age <= 3:  # 此处可精简
    print("婴儿")

# 上述情况使用if-elif-else会节省计算时间
if age < 0:
    print("未出生")
elif age <= 3:  # 运行此处时，age必定大于0
    print("婴儿")
elif age <= 6:  # 运行此处时，age必定大于3
    print("儿童")
else:
    print("HaHa")

# elif  else if
# 每一个elif都是对它上面所有表达式的否定



























