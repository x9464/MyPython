# -*- coding = utf-8 -*-
# @Time : 2021/1/29 16:13
# @Author: 肖兴
# @File ： hwNnm.py
# @Software : PyCharm


def hwNum(a):
    if a[::] == a[::-1]:
        print("该字符串是一个回文数")
    else:
        print("该字符串不是一个回文数")


if __name__ == '__main__':
    num = input()
    hwNum(num)