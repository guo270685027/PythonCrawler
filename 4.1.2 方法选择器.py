# -*- coding: utf-8 -*-
# @Time    : 2022/1/29 14:51
# @Author  : GXL
# @FileName: 4.1.2 方法选择器.py
# @Software: PyCharm
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
from bs4 import BeautifulSoup
import re
soup= BeautifulSoup(html,'lxml')
# print(soup.find_all(name='ul'))
# #调用了find_all （）方法，传入name 参数，其参数值为ul 。也就是说，我们想要查询所有ul节点，返回结果是列表类型，长度为2 ，每个元素依然都是bs4.element.Tag 类型
# print(type(soup.find_all(name="ul")[0]))
# #因为都是Tag 类型，所以依然可以进行嵌套查询。还是同样的文本，这里查询出所有u l 节点后，再继续查询其内部的li 节
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name="li"):
#         print(li.string)

# attrs
# print(soup.find_all(attrs={'id':'list-1'}))
# print(soup.find_all(attrs={'name':'elements'}))
# print(soup.find_all(class_='element'))
# print(soup.find_all(id='list-2'))

# text,text 参数可用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象
html2='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
# soups = BeautifulSoup(html2, 'lxml')
# print(soups.find_all(text=re.compile('link')))
#
# # 除了find_all （）方法，还有find （）方法，只不过后者返回的是单个元素，也就是第一个匹配的元素，而前者返回的是所有匹配的元素组成的列表。
# print(soup.find('li'))

# find_parents （）和find_parent （）： 前者返回所有祖先节点， 后者返回直接父节点。
# find_next_siblings （）和find_next_ sibling （）： 前者返回后面所有的兄弟节点， 后者返回后面第一个兄弟节点。
# find_previous_siblings （）和find_previous_sibling （）： 前者返回前面所有的兄弟节点， 后者返回前面第一个兄弟节点。
# find_all_next （）和find_next （）： 前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。
# find_all_previous （）和find_previous （） ：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。
print(soup.find_previous(id='elements'))