# -*- coding: utf-8 -*-

import os

filepath = 'C:\\Users\\Lei\\Desktop\\Python_Test\\'  # 文件所在路径
pathdir = os.listdir(filepath)  # 读取路径下的所有文件名
#print(pathdir)
for filename in pathdir:
    #print(filename)
    openname = filepath + filename
    mac_all = open(openname, 'r')
    #print(mac_all.readlines())
    mac_list = mac_all.readlines()
    list_index = 0
    for mac_line in mac_list:
        #print(mac_line.strip())
        if ('Intel(R) Ethernet Connection' in mac_line) is True:
            nic_name_index = mac_line.find(':')
            nic_name = mac_line[nic_name_index:]
            nic_mac = mac_list[list_index + 1]
            nic_mac_index = nic_mac.find(':')
            nic_mac = nic_mac[nic_mac_index:]
            print(filename.rstrip('.txt') + '\n' + nic_name.lstrip(': ') + nic_mac.lstrip(': '))
        list_index += 1