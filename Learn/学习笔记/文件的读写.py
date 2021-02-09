# -*- coding: utf-8 -*-

# open 函数的使用

device_files = open('C:\\Users\\root\\Desktop\\Workspace\\devices.txt', 'r')
ip_files = open('C:\\Users\\root\\Desktop\\Workspace\\IP_Lists.txt', 'r')
#print(files)
#devices_list = device_files.readlines()
#ip_list = ip_files.readlines()
#print(devices_list)
#print(ip_list)

#for devices_list in device_files.readlines():
    #print(devices_list)


#for ip_list in files2.readlines():
    #print(ip_list)

for ip in ip_files.readlines():
    if ip.startswith('172.16'):
        print(ip.strip())  # 删除换行符