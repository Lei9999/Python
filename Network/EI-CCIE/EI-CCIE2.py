#!/usr/bin/python
# -*- coding: utf-8 -*-

# 该脚本应用于CSR的Guest Shell中

from cli import cli  # 参考官方手册得来
import cli  # 参考官方手册得来
from sys import argv  # 用于读写文件

script, filename = argv  # 运行该脚本必须接文件名称参数"python test.py test1"

str_sh_ospf = cli.cli('show ip route ospf')
list_sh_ospf = str_sh_ospf.splitlines()  # 把得到的字符串进行分割装入列表中
len_list_ospf = len(list_sh_ospf)  # 计算列表的长度

traget = open(filename, 'w')
traget.truncate  # 先把文件清空

line1 = "*** Printing show ip route ospf ***"
line2 = "*** Only Display OSPF O Route ***"

print('''
%s
%s
''' % (line1, line2))

traget.write(line1)
traget.write("\n")
traget.write(line2)
traget.write("\n")
traget.write("\n")

num = 0
while num < len_list_ospf:
    match_ospf_only_O = list_sh_ospf[num]  # 从列表中按照下标进行取值
    n = match_ospf_only_O.find("O   ")  # 进行查找，若匹配则返回值为0，并赋予n
    # print(n)
    if n == 0:
        num = num - 1
        match_ospf_only_O = list_sh_ospf[num]  # 匹配后，将前一个下标的列表值并赋予变量
        print(match_ospf_only_O)  # 打印出变量
        traget.write(match_ospf_only_O)  # 将变量写入文件中
        traget.write("\n")  # 将回车写入文件中
        num = num + 1
        match_ospf_only_O = list_sh_ospf[num]  # 将匹配的该列表值赋予变量
        print(match_ospf_only_O)  # 打印出变量
        traget.write(match_ospf_only_O)  # 将变量写入文件中
        traget.write("\n")  # 将回车写入文件中
        num = num + 1
        continue  # 跳过当前循环中的剩余语句，然后继续下一次循环
    num = num + 1  # 在n不等于0的情况下说明未匹配，则列表下标+1，继续进行循环

print('''
*** The above has been written to the file \"ospf\" ***
''')
traget.close()  # 等同于关闭并保存
