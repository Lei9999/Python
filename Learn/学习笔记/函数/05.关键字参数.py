'''
概念：允许函数调用时参数的顺序与定义时不一致
'''

def myPrint(str_ex,age):
    print(str_ex,age)

#使用关键字参数
myPrint(age = 18, str_ex = "Shilei is a good man!")
