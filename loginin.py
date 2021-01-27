# -*- coding = utf-8 -*-
# @Time : 2021/1/24 20:24
# @Author: 肖兴
# @File ： loginin.py
# @Software : PyCharm


def login(n, m):
    dic = {"admin": "admin@123", "guess": "123456", "my": "my_666"}
    if dic[n] == m:
        print("登录成功")
    else:
        print('您输入的账号或密码不正确')


def main():
    inputs = input("请输入账号：")
    inputs1 = input("请输入密码：")
    login(inputs, inputs1)


if __name__ == '__main__':
    main()
