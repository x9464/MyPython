# -*- coding = utf-8 -*-
# @Time : 2021/1/21 12:47
# @Author: 肖兴
# @File ： mode.py
# @Software : PyCharm


import random
getNum = input()
if getNum == 'GET':
    ran = random.randint(100000, 999999)
print(ran)