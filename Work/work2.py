# -*- coding: utf-8 -*-

'''
使用Python paramiko 库，批量登录设备，获取配置信息，逐个保存到文本中
思路
1、读取文本文档，获取设备的IP地址，并放入list中
2、遍历list中的IP地址，进行ssh登录
3、执行命令，收集结果
4、保存收集的结果到文件中，文件以IP地址开头，并附加日期以及时间
'''

import os
import paramiko
import time
from datetime import datetime

input_devices_ip_tips = ("""
请输入设备信息文件的UNC路径：
-例(Windows)：C:\\Users\\root\Desktop\\devices_ip.txt
-例(Linux)：/home/user1/devices.txt
""")
input_conf_save_tips = ("""
请输入设备配置文件保存的目录：
-例(Windows)：C:\\Users\\root\\Desktop\\conf\\
-例(Linux)：/home/user1/conf/
""")
now_time = datetime.now()
now_time = now_time.strftime("%Y%m%d" + "_" + "%H%M")  # 获取当前时间，格式为：“20210101_1130”
ssh_username = 'python'
ssh_password = 'python'
devices_ip_files = input(input_devices_ip_tips)  # 获取设备文件所在位置
input_conf_save_dir = input(input_conf_save_tips)  # 获取设备配置文件保存路径

# 读取文件中的IP地址并保存在临时列表中
with open(devices_ip_files, mode='r') as r_ip:
    devices_ip_temp_list = r_ip.readlines()

# 将列表中空格以及"\n"去掉，得到最终的设备IP地址列表
devices_ip_list = [x.strip() for x in devices_ip_temp_list if x.strip()!='']
#print(devices_ip_list)

# ssh模块
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

devices_ip = ()
for devices_ip in devices_ip_list:
    config_file_name = (
    input_conf_save_dir
    + devices_ip
    + "_"
    + now_time
    + ".txt"
    )

    ssh_client.connect(
        hostname=devices_ip, 
        username=ssh_username, 
        password=ssh_password, 
        look_for_keys=False
        )
    ssh_command = ssh_client.invoke_shell()

    print('\n已成功登录设备' + devices_ip + '，正在保存配置，请稍等...')

    ssh_command.send('terminal length 0\n')
    ssh_command.send('terminal width 0\n')
    ssh_command.send('show running-config\n')
    time.sleep(3)
    output = ssh_command.recv(65535).decode('ascii')
    output = output[output.find('show running-config'):]  # 截取从"show running-config"开始到尾部

    #将得到的结果写入文件中
    with open(config_file_name, mode='a') as w_cfg:
        w_cfg.write(output)
    print('设备"%s"配置已保存完成！' % (devices_ip))
    ssh_client.close()

print('\n所有设备配置已保存完成！')