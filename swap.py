# -*- coding = utf-8 -*-
# @Time : 2021/1/29 15:54
# @Author: 肖兴
# @File ： swap.py
# @Software : PyCharm


def swap(x):
    a = min(x)
    a1 = x.index(a)
    x[-1], x[a1] = x[a1], x[-1]
    b = max(x)
    b1 = x.index(b)
    x[0], x[b1] = x[b1], x[0]
    for item in x:
        print(item, end=",")


if __name__ == '__main__':
    ls = [3, 1, 9, 8, 0, 4, 6, 7]
    swap(ls)
