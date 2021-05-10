import string
import os


def get_disklist():
    disk_list = []
    for c in string.ascii_uppercase:
        disk = c + ':'
        if os.path.isdir(disk):
            disk_list.append(disk)
    return disk_list


if __name__ == '__main__':
    print(get_disklist())
