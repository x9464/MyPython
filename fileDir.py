# -*- coding = utf-8 -*-
# @Time : 2021/1/27 15:55
# @Author: 肖兴
# @File ： fileDir.py
# @Software : PyCharm


import os


def main():
    road = input()
    name = os.listdir(road)
    for item in name:
        print(item)

main()