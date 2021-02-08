# -*- coding = utf-8 -*-
# @Time : 2021/2/8 14:56
# @Author: 肖兴
# @File ： dayNum.py
# @Software : PyCharm


import datetime as data


# 判断是否为闰年
def judge(year):
    temp = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        temp = True
    return temp


# 计算日期
def cal(year, month, day):
    ls = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if month > 2:
        res = judge(year)
        for i in range(month):
            days += ls[i]
        if res:
            days += 1
        days = days + day
    else:
        for i in range(month):
            days += ls[i]
        days += day
    return days


# 输入日期并且判断合法性
def recin():
    getIn = input()
    if '/' in getIn or '-' in getIn or '年' in getIn:
        newInput = getIn.replace('/', '-').replace('年', '-').replace('月', '-').replace('日', '')
        ls = newInput.split('-')
        y = eval(ls[0])
        m = eval(ls[1])
        d = eval(ls[2])
        da = cal(y, m, d)
        print(getIn, "是", ls[0], "年的第{}天".format(da))
    else:
        print("您输入的内容不是一个日期")


if __name__ == '__main__':
    recin()
