# -*- coding: utf-8 -*-

'''
通过paramiko ssh设备并拉取配置的基本语句
paramiko 好比手动挡汽车，netmiko则是自动挡汽车
所以先从手动挡汽车学起
'''

import paramiko
import time

device_ip = '192.168.103.238'
device_username = 'python'
device_password = 'python'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(
    hostname=device_ip, 
    username=device_username, 
    password=device_password, 
    look_for_keys=False
    )
ssh_command = ssh_client.invoke_shell()
ssh_command.send('terminal length 0\n')
ssh_command.send('terminal width 0\n')
ssh_command.send('show running-config\n')
time.sleep(3)
ssh_output = ssh_command.recv(65535).decode('ascii')
ssh_client.close()

#print(ssh_output)
# 现在有一个问题，就是收到的东西也包括先前输入的命令，想办法给过滤掉
# 只保留从'show running-config'开始

output_index = ssh_output.find("show running-config")  # 找到第一次出现'show run'的下标
print(output_index)  # 打印下标
device_cfg = ssh_output[output_index:]  # 从给定下标处开始截取到结尾

# 上述语句可以简化为一句
ssh_output = ssh_output[ssh_output.find('show running-config'):]
print(ssh_output)