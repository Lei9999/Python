"""
默认参数
概念：调用参数时，如果没有传递参数，则使用默认参数
注意：默认参数必须放在最后
"""


def myPrint(str_ex="Shilei", age=18):
    print(str_ex, age)


myPrint()
myPrint("Zhangzhe", 20)


# 将来使用默认参数，将默认参数放在最后
def myPrint_1(str_ex1, age=18):
    print(str_ex1, age)


myPrint_1("Zhangzhe")
