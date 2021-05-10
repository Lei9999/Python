# -*- coding: utf-8 -*-

"""
定义一个函数，获取当前OS的磁盘分区信息，不含隐藏分区。
"""

import string
import os


def get_volume():
    volume_list = []
    for _ in string.ascii_uppercase:
        volume = _ + ':'
        if os.path.isdir(volume):
            volume_list.append(volume)
    return volume_list


if __name__ == '__main__':
    print(get_volume())
