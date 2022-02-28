# -*- coding: utf-8 -*-
# @Time    : 2022/1/23 15:21
# @Author  : GXL
# @FileName: 4.1.1 解析库.py
# @Software: PyCharm
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# # print(soup.title.string)
# # soup.title.string输出文本的值，soup.title输出代码
# print(soup.p)
# # 当有多个节点时，这种选择方式只会选择到第一个匹配的节点，其他的后面节点都会忽略。
# print(soup.head)
#
# #获取名称,可以利用name 属性获取节点的名称。这里还是以上面的文本为例，选取title 节点，然后调用name属性就可以得到节点名称
# print(soup.title.name)
# # 提取属性
# print(soup.a.attrs)
# print(soup.a.attrs['href'])
# # print(soup.a["href"])
#
# #获取内裤可以利用string 属性获取节点元素包含的文本内容
# print(soup.title.string)
#
# #嵌套选择
# print(soup.head.title.string)
# #我们在Tag 类型的基础上再次选择得到的依然还是Tag 类型，每次返回的结果都相同，所以这样就可以做嵌套选择了

# print(soup.p.contents)
#返回结果为列表类型，返回p的直接子节点
# for children in soup.p.children:#这个返回是生成器类型，需要用for 循环
#     print(children)

# 父节点和祖先节点 ，如果要获取某个节点元素的父节点，可以调用parent 属性：
# print(soup.p.parent)
# 输出的仅仅是p 节点的直接父节点，而没有再向外寻找父节点的祖先节点
# 如果想获取所有的祖先节点，可以调用parents 属性：返回的是生成器类型，需要用for循环遍历

# 兄弟节点；获取同级的节点
# print(soup.a.next_sibling)   #后面的节点
# print(soup.a.previous_sibling)  #前面的节点
# print(list(soup.a.previous_siblings))
# print(list(soup.a.next_siblings))

# 提取信息
print(list(soup.a.next_siblings)[1].attrs['href'])
print(soup.prettify())

