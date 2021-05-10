# -*- coding: utf-8 -*-

"""输入一个文件名，将"OK"写入该文件中并保存在当前目录下"""

inputFileName = input('请输入文件名：')
# helloFile = open(input1, 'w')
with open(inputFileName, 'w') as target:
    target.write('OK')  # 将“OK”写入文件中

# file_dir = r'C:\Users\Lei\Desktop\192.168.0.1_20210107_20:37:32.txt'
# with open(file_dir, mode='w', encoding='utf-8') as w_cfg:
#    w_cfg.write("OK")
