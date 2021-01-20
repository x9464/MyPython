# -*- coding = utf-8 -*-
# @Time : 2021/1/20 18:36
# @Author: 肖兴
# @File ： numCal.py
# @Software : PyCharm


def main():
    num = (input())
    nums = 0
    ls = [1, 2, 3, 4, 5]
    for i in ls:
        nums += eval(num*i)
    for j in ls[0:4]:
        nums += eval(num*j)
    print("{}+{}+{}+{}+{}+{}+{}+{}+{}={}".format(eval(num*ls[0]), eval(num*ls[1]), eval(num*ls[2]), eval(num*ls[3]), eval(num*ls[4]),
          eval(num*ls[3]), eval(num*ls[2]), eval(num*ls[1]), eval(num*ls[0]), nums))


if __name__ == '__main__':
    main()
