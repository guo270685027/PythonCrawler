# -*- coding: utf-8 -*-
# @Time    : 2022/1/30 9:54
# @Author  : GXL
# @FileName: 5.1.1 TXT 文本存储.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests
url ='https://www.csdn.net/'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}
html = requests.get(url,headers).text
soup = BeautifulSoup(html,'lxml')
file =open('1.txt','a',encoding='utf-8')
file.write('\n'.join(list(html)))
file.close()
