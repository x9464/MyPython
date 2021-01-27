# -*- coding = utf-8 -*-
# @Time : 2021/1/21 12:47
# @Author: 肖兴
# @File ： mode.py
# @Software : PyCharm


import random
getNum = input()
while 1:
    if getNum == 'GET':
        ran = random.randint(100000, 999999)
        print(ran)
        break
    elif getNum != 'GET':
        print("输入错误,请重新输入！")
        getNum = input()