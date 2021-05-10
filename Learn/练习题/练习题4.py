# 输入一个单词，确认该单词在字符串中出现的次数
# 使用字典功能来实现

w = input("请输入一个单词：")
dict_str = {}  # word:次数

str1 = "shilei is a good man ! shilei is a nice man ! shilei is a hands man ! shilei is a lucky man ! shilei is a great man ! shilei is a cool man !"

list_str = str1.split(" ")  # 以空格切割字符串
# print(list_str)
# print(str.count(w))

for v in list_str:  # 循环处理列表中每个元素
    c = dict_str.get(v)  # 以元素当做key去字典中提取数据
    if c is None:
        dict_str[v] = 1  # 当没有提取到数据时，变将该元素作为key，value赋值1
    else:
        dict_str[v] += 1  # 如果提取到，将ley对应的value+1
print(dict_str)
print(dict_str[w])  # 将输入的字符串当做key，并去字典中提取value

# 歌词解析
