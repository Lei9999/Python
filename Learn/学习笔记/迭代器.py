from collections import Iterable
from collections import Iterator
'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象（Iterable）
可以使用isinstance()去判断一个对象是否是Iterable

可以直接作用于for的数据类型一般分两种：
1.集合数据类型：list、tuple、dict、set、string
2.generator：包括生成器和带 yield 的 generator function
'''
print(isinstance([], Iterable))  # True 可迭代对象
print(isinstance((), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance("", Iterable))  # True
print(isinstance((x for x in range(10)), Iterable))  # True
print(isinstance(1, Iterable))  # False


'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值
直到最后抛出一个StopIteration错误，表示无法继续返回下一个值

可以被next()函数调用并不断返回下一个值的对象称为迭代器（Iterator对象）

可以使用isinstance()函数判断一个是否是Iterator对象
'''
print(isinstance([], Iterator))  # False
print(isinstance((), Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance("", Iterator))  # False
print(isinstance((x for x in range(10)), Iterator))  # True

# 迭代器
list_ex = (x for x in range(5))
print(next(list_ex))
print(next(list_ex))
print(next(list_ex))
print(next(list_ex))
print(next(list_ex))

# 转为Iterator对象
a = iter([1, 2, ,3 ,4, 5])
print(next(a))
print(next(a))

print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(''), Iterator))




