# -*- coding = utf-8 -*-
# @Time : 2021/1/27 19:52
# @Author: 肖兴
# @File ： wordCounts.py
# @Software : PyCharm


def main():
    f = open('e:\\demo.txt', 'r')
    for line in f:
        words = line.split()
        # print(words)
    word = input()
    count = 0
    for i in words:
        if word == i:
            count += 1
    print("{}在文件中出现了{}次".format(word, count))


main()
