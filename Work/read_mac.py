# -*- coding: utf-8 -*-

import os

filepath = 'C:\\Users\\Lei\\Desktop\\MAC_List\\'  # 文件所在路径
pathdir = os.listdir(filepath)  # 读取路径下的所有文件名并生成为列表
# print(pathdir)
# 循环依次打开每一个文件进行操作
for filename in pathdir:
    # print(filename)
    openfile_name = filepath + filename

    # read_mac_all = open(openfile_name, 'r')
    # mac_list = read_mac_all.readlines()

    # 打开文件将内容读取到列表中
    with open(openfile_name, 'r') as read_mac_all:
        mac_list = read_mac_all.readlines()
    # print(mac_all.readlines())

    list_index = 0  # 定义列表下标从0开始
    # 循环每一个列表元素
    for mac_line in mac_list:
        # print(mac_line.strip())
        if ('Intel(R) Wi-Fi 6 AX200' in mac_line) is True:  # 如果列表元素中含有关键字则进行下列进行操作
            nic_name_index = mac_line.find(':')  # 找到冒号所在字符串的下标
            nic_name = mac_line[nic_name_index:]  # 截取从该下标开始往后的字符
            nic_mac = mac_list[list_index + 1]  # 并读取下一个列表元素
            nic_mac_index = nic_mac.find(':')  # 找到冒号所在字符串的下标
            nic_mac = nic_mac[nic_mac_index:]  # 截取从该下标开始往后的字符
            # 打印出来，将文件名字删除'.txt'后缀，网卡名字删除': '前缀和尾部换行符，再加上MAC地址（删除': '前缀）
            print(filename.rstrip('.txt') + ',' + nic_name.lstrip(': ').rstrip('\n') + ',' + nic_mac.lstrip(': '))
            # 保存到文件中
            with open('C:\\Users\\Lei\\Desktop\\WLAN_MAC.csv', 'a', encoding='utf-8') as files:
                files.write(filename.rstrip('.txt') + ',' + nic_name.lstrip(': ').rstrip('\n') + ',' + nic_mac.lstrip(': '))
        list_index += 1  # 如果当前列表元素中没有找到需要的关键字，列表下标+1
