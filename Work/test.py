# -*- coding: utf-8 -*-
# 用于测试部分语句

'''
使用Python paramiko 库，批量登录设备，获取配置信息，逐个保存到文本中
思路
1、读取文本文档，获取设备的IP地址，并放入list中
2、遍历list中的IP地址，进行ssh登录
3、执行命令，收集结果
4、保存收集的结果到文件中，文件以IP地址开头，并附加日期以及时间
'''

import os
from datetime import date, datetime

#now_time = datetime.now()
#now_time = now_time.strftime("%Y%m%d%X")
#print(now_time)

input_conf_save_dir = input('请输入一个路径：')  # 获取设备配置文件保存路径
#conf_save_dir = input_conf_save_dir.replace('\\', '\\')
#conf_save_dir = r'C:\\Users\\root\\'
#conf_save_dir = os.path.dirname(input_conf_save_dir)
#print(dir_list)
#print(conf_save_dir)

now_time = datetime.now()
now_time = now_time.strftime("%Y%m%d" + "_" + "%H%M")  # 这个地方呢，如果加确切的时间带有':'，open是无法识别的
config_file_name = (
    input_conf_save_dir
    + "192.168.0.1"
    + "_"
    + now_time
    + ".txt"
)
#print(config_file_name)
with open(config_file_name, mode='w', encoding='utf-8') as w_cfg:
    w_cfg.write("OK")