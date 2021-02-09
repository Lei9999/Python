# -*- coding: utf-8 -*-

'''
文件的读取
open()函数的使用：r/w/a/r+/w+/a+
'''

# r 模式

device_file = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r')
ip_file = open('C:\\Users\\root\\Desktop\\Workspace\\IP_Lists.txt', 'r')

#print(files)
#device_list = device_file.readlines()
#ip_list = ip_file.readlines()
#print(device_list)
#print(ip_list)

#for device_list in device_file.readlines():
#    print(device_list)


#for ip_list in ip_file.readlines():
#    print(ip_list)

#for ip in ip_file.readlines():  # 输出172.16开头的IP地址
#    if ip.startswith('172.16'):
#        print(ip.strip())  # 删除换行符

device_file.close()
ip_file.close()

'''
文件的写入
write()函数
在使用write()函数的时候，open()函数的r模式不支持，其他五种模式均支持
'''

# r+ 以读写的方式打开已存在的文件，若文件不存在，则报错

device_file_w = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r+', encoding='utf-8')
for device_list in device_file_w.readlines():  # 输出改动之前的数据
    print(device_list.strip())
device_file_w.seek(0)  # 将光标定位到文件开头的位置
#print(device_file_w.tell())  # 打印出当前光标所在位置

# 写入的时候发现换行符\n也被替换掉了，因为Sangfor字符长度正好是Cisco\n的长度
#device_file_w.write('Sangfor\n')  # 追加换行符\n
#device_file_w.close()
#device_file_w = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r+')
#for device_list in device_file_w.readlines():
#    print(device_list.strip())

print('~' * 10)  # 打印神奇的分隔符

# 我们使用相同长度的字符串进行替换
#device_file_w.write('11111')
device_file_w.close()  # 关闭并保存文件
# 再次打开文件进行输出
device_file_w = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r')
for device_list in device_file_w.readlines():
    print(device_list.strip())
device_file_w.close()

# w/w+ 模式，直接覆盖原有内容，w只用于写入，w+读写

#device_file_w = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'w+', encoding='utf-8')
#device_file_w.write('Cisco\nJuniper\nH3C\n')
#device_file_w.close()
# 上面代码注释掉了是为了不影响下面的实验
print('-' * 10)  # 打印神奇的分隔符
device_file_w = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r')
for device_list in device_file_w.readlines():
    print(device_list.strip())
device_file_w.close()
print('^' * 10)

# a/a+，在文档尾部追加内容，原有内容不会覆盖，a仅追加方式,a+读写方式

device_file_w = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'a+', encoding='utf-8')
for device_list in device_file_w.readlines():
    print(device_list.strip())
device_file_w.seek(0)  # 光标回到文档开头，测试是否是追加
# 这个位置无论是否加光标，都是追加模式
device_file_w.write('+++++\n')
device_file_w.close()
device_file_w = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r', encoding='utf-8')
for device_list in device_file_w.readlines():
    print(device_list.strip())
device_file_w.close()

# with 语句，用于自动关闭打开的文件
device_file_w = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r', encoding='utf-8')
print(device_file_w.closed)  # 此时返回值是False
device_file_w.close()

with open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r', encoding='utf-8') as files:
    files.read()
print(files.closed)  # 返回值是True