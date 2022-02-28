# -*- coding: utf-8 -*-
# @Time    : 2022/1/22 21:18
# @Author  : GXL
# @FileName: 3.3.3 正则表达式3.py
# @Software: PyCharm
import re

# sub方法,借助它来修改文本
# content = "54aKS4yrsoiRS4ixSL2g"
# content = re.sub('\d+','',content)
# #第一个参数传入\d＋来匹配所有的数字，第二个参数为替换成的字符串(如果去掉该参数的话，可以赋值为空），第三个参数是原字符串
# print(content)
html='''＜ div id="songs-list" >
<h2 class ＝"title"〉经典老歌＜/h2>
<p class=” introduction”>
经典老歌
</p>
<ul id=”list” class=”list-group”>
<li data-view="2”>一路上有你</li>
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
html = re.sub('<a.*?>|</a>','',html)
html = re.findall('<li.*?>(.*?)</li>',html,re.S)

for i in html:
    print(re.sub('\n','',i))

# compile()方法这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用。
content1 = '''2022-1-22 22:
52'''
content2 = '2022-1-22 22:53'
content3 = '2022-1-22 22:54'
pattern = re.compile('\d{2}:.*?\d{2}',re.S)
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)
print(result1)
print(result2)
print(result3)
#另外compile（）还可以传入修饰符，例如re.S等修饰符，这样在search（） 、findall（）等方法中就不需要额外传了。
#所以compile（）方法可以说是给正则表达式做了一层封装，以使我们更好地复用
