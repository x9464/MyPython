# -*- coding = utf-8 -*-
# @Time : 2021/1/27 15:45
# @Author: 肖兴
# @File ： oddNum.py
# @Software : PyCharm


def main():
    ls = []
    for i in range(30):
        ls.append(i)
    ls.sort(reverse=True)
    print("30以内从大到小的12个奇数为：")
    for i in ls[:24]:
        if i % 2 == 0:
            continue
        else:
            print(i)


main()
