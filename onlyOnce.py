# -*- coding = utf-8 -*-
# @Time : 2021/1/21 12:01
# @Author: 肖兴
# @File ： onlyOnce.py
# @Software : PyCharm


def main():
    ls = [2, 8, 6, 2, 7, 3, 9, 2, 8, 6, 7, 9, 1]
    ls_dict = {}
    ls1 = []
    for item in ls:
        ls_dict[item] = ls_dict.get(item, 0) + 1
    for key, val in ls_dict.items():
        if val == 1:
            ls1.append(key)
    print("只出现一次的数字是{}和{}".format(ls1[0], ls1[1]))


main()
