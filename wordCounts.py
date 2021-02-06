# -*- coding = utf-8 -*-
# @Time : 2021/1/27 19:52
# @Author: 肖兴
# @File ： wordCounts.py
# @Software : PyCharm


import re


def main():
    with open('e:\\par\demo.txt', 'r') as f:
        arr = []
        for line in f:
            arr.append(line)
    words = "".join(arr)
    words = words.replace(',', '').replace('.', '')
    print(words)
    print(arr)
    arr = words.split()
    print(arr)
    word = input()
    count = 0
    for i in arr:
        if word == i:
            count += 1
    print("{}在文件中出现了{}次".format(word, count))


main()
