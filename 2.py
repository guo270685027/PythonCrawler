# -*- coding: utf-8 -*-
# @Time    : 2022/2/1 18:56
# @Author  : GXL
# @FileName: 2.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests
import re
url = 'https://m.60wx.cc/86/86724/26244935.html'
headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}
html = requests.get(url,headers=headers).content
print(html)
soup =BeautifulSoup(html,'lxml')
