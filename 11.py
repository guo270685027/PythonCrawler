# -*- coding: utf-8 -*-
# @Time    : 2022/1/23 15:16
# @Author  : GXL
# @FileName: 11.py
# @Software: PyCharm
def go():
    for i in range(5):
        yield i
for h in go():
    print(h)
