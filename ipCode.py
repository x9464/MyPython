# -*- coding = utf-8 -*-
# @Time : 2021/1/29 15:21
# @Author: 肖兴
# @File ： ipCode.py
# @Software : PyCharm


def main():
    ip = input()
    with open('E://par/white_list.txt', 'r') as f:
        ipArr = []
        for line in f:
            ipArr.append(line)
    words = "".join(ipArr)
    words = words.replace('', '')
    ipArr = words.split()
    if ip in ipArr:
        print("该IP地址可以访问网络")
    else:
        print("该IP地址不允许访问网络")


main()
