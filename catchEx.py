# -*- coding = utf-8 -*-
# @Time : 2021/2/6 14:06
# @Author: 肖兴
# @File ： catchEx.py
# @Software : PyCharm


def main(x, y):
    try:
        if x / y:
            res = x / y
            print(res)
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    a, b = eval(input())
    main(a, b)
