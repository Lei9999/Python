# -*- coding: utf-8 -*-

# open 函数的使用

files1 = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r')
files2 = open('C:\\Users\\root\\Desktop\\Workspace\\IP_Lists.txt', 'r')
#print(files)
#devices_list = files1.readlines()
#ip_list = files2.readlines()
#print(devices_list)
#print(ip_list)

for devices_list in files1.readlines():
    print(devices_list)

for ip_list in files2.readlines():
    print(ip_list)