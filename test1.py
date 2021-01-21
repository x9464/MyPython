# -*- coding = utf-8 -*-
# @Time : 2021/1/20 17:44
# @Author: 肖兴
# @File ： test1.py
# @Software : PyCharm


ls = [1, 2, 3, 4, 3, 3, 4, 5, 6, 5, 7, 7, 6]
ls1 = []
for item in ls:
    counts = 0
    if item not in ls1 and counts == 0:
        ls1.append(item)
        counts += 1
    else:
        ls1.remove(item)
        counts -= 1
print(ls1)