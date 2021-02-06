# -*- coding = utf-8 -*-
# @Time : 2021/2/6 14:41
# @Author: 肖兴
# @File ： numSum.py
# @Software : PyCharm


def main():
    sums = 0
    for i in range(1000):
        if i % 2 == 0:
            if i == 40 or i == 48:
                continue
            sums += i
        else:
            continue
        if sums >= 25000:
            print("0到1000之间(40,48跳过，大于等于25000跳出)偶数的和为:{}".format(sums))
            break


main()

