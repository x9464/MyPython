# -*- coding = utf-8 -*-
# @Time : 2021/2/9 13:28
# @Author: 肖兴
# @File ： price.py
# @Software : PyCharm


class Item:
    ItemCode = ["c_101", "c_102"]
    ItemName = ["HUAWEI Mate30 Pro", "XIAOMI 10 Pro"]
    UnitPrice = [5000.00, 4699.00]


class Order(Item):
    def getOrderAmount(self,itemCode, itemCount):
        itemCount = eval(itemCount)
        name = Item.ItemCode.index(itemCode)
        nPrice = Item.UnitPrice[name]
        priceSum = itemCount * nPrice
        print(priceSum)


if __name__ == '__main__':
    a, b = map(str, input().split(','))
    price = Order()
    price.getOrderAmount(a,b)