"""
元祖
将多个对象保存到一起，近似的看做列表
元祖的一大特征类似于字符串，它们是不可变的
不能编辑或更改元祖
作用：
保证某一句语句或某一用户定义的函数可以安全地采用一组数值
"""
# 创建空的元祖
tuple1 = ()
print(tuple1)
# 创建带有元素的元祖
# 元祖中的元素的类型可以不同
tuple2 = (1, 2, 3, 'good', True)
print(tuple2)
# 定义只有一个元素的元祖
tuple3 = (1, )
print(tuple3)
print(type(tuple3))

'''
元祖元素的访问
格式：元组名[下标]
下标从0开始
'''
tuple4 = (1, 2, 3, 4, 5)
print(tuple4[0])  # 打印1
# print(tuple4[5])  # 下标超过范围
print(tuple4[-1])  # 获取最后一个元素
print(tuple4[-2])  # 获取倒数第二个元素
print(tuple4[-5])  # 元祖中第一个元素
# print(tuple4[-6])  # 越界

'''
修改元祖
'''
tuple5 = (1, 2, 3, 4, [5, 6, 7])
# tuple5[0] = 100  # 报错，元祖不能变（元素）
# tuple5[-1] = [1, 2, 3]
tuple5[-1][0] = 500  # 元祖中的元素列表可以改变
print(tuple5)

# 删除元祖
tuple6 = (1, 2, 3)
del tuple6
# print(tuple6)  # 已删除无法打印

'''
元祖的操作
'''
# 元祖相加
t7 = (1, 2, 3)
t8 = (4, 5, 6)
t9 = t7 + t8
print(t9)

# 元祖重复
t10 = (1, 2, 3)
print(t10 * 3)

# 判断元素是否在元祖中
t11 = (1, 2, 3)
print(1 in t11)
print(4 in t11)

# 元祖的截取
# 格式:元祖名[开始下标:结束下标]
# 从"开始下标"开始截取,截取到"结束下标"之前
t12 = (1, 2, 3, 4, 5, 6, 7, 8)
print(t12[0:3])  # 得到(1, 2, 3)
print(t12[:3])
print(t12[3:])

# 二维元祖
# 二维元祖的元素是一维元祖
t13 = ((1, 2, 3), (4, 5, 6), (7, 8))
print(t13)
print(t13[1][1])  # 得到5

# 元祖的方法
# len()	返回元祖中元素的个数
t14 = (1, 2, 3, 4, 5)
print(len(t14))
# max()	返回元祖中的最大值
print(max(t14))
# min()	返回元祖中的最小值
print(min(t14))

# 将列表转成元祖
list1 = [1, 2, 3]
t15 = tuple(list1)
print(t15)

# 元祖的遍历
for i in t15:
	print(i)


