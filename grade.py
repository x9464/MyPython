# -*- coding = utf-8 -*-
# @Time : 2021/2/6 14:26
# @Author: 肖兴
# @File ： grade.py
# @Software : PyCharm


def main():
    MyGrade = 361
    Grade = 451
    result = "通过一本录取分数线" if MyGrade > Grade else "未通过一本录取分数线"
    print(" 您的高考总分：", MyGrade, "\n", "第一批本科录取分数线: ", Grade, "\n", "高考结果：", result)


main()
