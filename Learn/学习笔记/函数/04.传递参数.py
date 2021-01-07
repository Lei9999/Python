'''
值传递：传递的是不可变类型
string，tuple，number是不可变
'''
def func1(num):
    num = 10

temp = 20
func1(temp)  #num = temp
print(temp)  #打印结果为20

'''
引用传递：传递的是可变类型
list，dict，set是可变的
'''

def fun2(list_ex):
    list_ex[0] = 100

list_1 = [1, 2, 3, 4]
fun2(list_1)
print(list_1)  #list_1[0] = 改为100
