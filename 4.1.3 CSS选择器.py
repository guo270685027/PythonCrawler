# -*- coding: utf-8 -*-
# @Time    : 2022/1/30 9:44
# @Author  : GXL
# @FileName: 4.1.3 CSS选择器.py
# @Software: PyCharm
from bs4 import BeautifulSoup

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup =BeautifulSoup(html,'lxml')
print(soup.select('ul li'))
print(soup.select('.element'))
print(soup.select('.list-small'))
print(soup.select('#list-2'))
print(soup.select('ul')[0])

# 获取文本
for i in soup.select('ul'):
    for m in i.select('li'):
        print(m.get_text())