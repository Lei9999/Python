# -*- coding: utf-8 -*-
# 用于测试部分语句

import os
from datetime import date, datetime

#now_time = datetime.now()
#now_time = now_time.strftime("%Y%m%d%X")
#print(now_time)

input_conf_save_dir = input()  # 获取设备配置文件保存路径
#conf_save_dir = input_conf_save_dir.replace('\\', '\\')
#conf_save_dir = r'C:\\Users\\root\\'
#conf_save_dir = os.path.dirname(input_conf_save_dir)
#print(dir_list)
#print(conf_save_dir)

now_time = datetime.now()
now_time = now_time.strftime("%Y%m%d%X")
config_file_name = (
    input_conf_save_dir
    + "192.168.0.1"
    + "_"
    + now_time
    + "_"
    + ".txt"
)
print(config_file_name)
#with open(r'C:\Users\root\desktop\exe.txt', mode='w', encoding='utf-8') as w_cfg:
#    w_cfg.write("OK")