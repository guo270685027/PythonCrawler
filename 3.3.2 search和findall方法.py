# -*- coding: utf-8 -*-
# @Time    : 2022/1/21 21:21
# @Author  : GXL
# @FileName: 3.3.2 search和findall方法.py
# @Software: PyCharm
import re
#search （）方法的用法，它可以返回匹配正则表达式的第一个内容
html='''＜ div id="songs-list" >
<h2 class ＝"title"〉经典老歌＜/h2>
<p class=” introduction”>
经典老歌
</p>
<ul id=”list” class=”list-group”>
<li data-view="2”〉一路上有你</li>
<li data-view="7”>
<a href="/2.mp3" singer=”任贤齐”>一路上有你</a>
</li>
<li data-view=”4” class=”active">
<a href="/3.mp3" singer=”齐泰”>往事随风</a>
</li>
<li data-view=“6”><a href="/4.mp3" singer=”beyond”>光辉岁月</a></li>
<li data-view=”5”><a href="/5.mp3" singer=”陈慧琳”>记事本</a></li>
<li data-view=”5’'>
<a href ＝”/6.mp3” singer=”邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
# result = re.search('<li.*?active.*?singer＝”(.*?)”>(.*?)</a>',html,re.S)
# print(result)
# print(result.group(1),result.group(2))

# findall()方法
result = re.findall('<li.*?href="(.*?)".*?singer=”(.*?)”>(.*?)</a>.*?</li>',html,re.S)
print(result)
for res in result:
     print(res)
     print(res[0],res[1],res[2])



