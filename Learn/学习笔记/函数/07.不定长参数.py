'''
不定长参数
概念：能处理比定义时更多的参数
'''

#加了星号(*)的变量存放所有未命名的变量参数
#如果在函数调用时没有制定参数，它就是一个空元祖
def func(name, *arr):
    print(name)
    print(type(arr))
    for x in arr:
        print(x)

func("Shilei", "Zhangzhe", "...")

def mySum(*l):
    sum_ex = 0
    for i in l:
        sum_ex += i
    return sum_ex

print(mySum(1, 2, 3, 4))

#**代表键值对的参数字典，和*所代表的意义类似
def func_2(**kwargs):
    print(kwargs)
    print(type(kwargs))

func_2(x = 1, y = 2, z =3)  #必须以字典的形式进行传参

#可以传入任何形式的参数
def func_3(*args, **kwargs):
    pass  #代表一个空语句
