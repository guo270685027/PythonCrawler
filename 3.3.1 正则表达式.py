# -*- coding: utf-8 -*-
# @Time    : 2022/1/20 21:47
# @Author  : GXL
# @FileName: 3.3.1 正则表达式.py
# @Software: PyCharm
import re

# 常用匹配方法match   match （）方法是从字符串的开头开始匹配的，一旦开头不匹配，那么整个匹配就失败了。
content = 'hello 123 4567 world_this is a regex demo'
print(len(content))
result = re.match('^hello\s\d{3}\s(\d{4})\s\w{10}',content)
result2 = re.match('hello.*o',content)
#match （）方法中，第一个参数传入了正则表达式，第二个参数传入了要匹配的字符串
# .*代表任意字符
print(result)
print(result.group())
#group()方法可以输出匹配到的内容
print(result.span())
#span （）方法可以输出匹配的范围，结果是（ 0, 25 ），这就是匹配到的结果字符串在原字符串中的位置范围。
print(result.group(1))
#将数字部分的正则表达式用（）括起来， 然后调用了group(1）获取匹配结果。
print(result2.group())


# 贪婪匹配
result3 = re.match('^h.*(\d+).*',content)
print(result3.group(1))
# *尽量匹配多的字符，+代表1个或无数个，*代表0个或无数个
# 非贪婪匹配的写法是．
result4 = re.match('^.*?(\d+).*?',content)
print(result4.group())
print(result4.group(1))
#在做匹配的时候，字符串中间尽量使用非贪婪匹配，也就是用．*?代替.*   但是如果.*?在结尾匹配可能就没有内容

# 修饰符
content1 = """hello 124567 world_this
is a regex demo
"""
result5 = re.match('^he.*?(\d+).*',content1,re.S)
print(result5.group(1))
# re.S使．匹配包括换行在内的所有字符
# re.I 使匹配对大小写不敏感

# 转义字符
content2 ='(www.百度.com)'
result6 = re.match('\(www\.百度\.com\)',content2)
print(result6.group())
#当遇到用于正则匹配模式的特殊字符时，在前面加反斜线转义一下即可。例如． 就可以用＼ ． 来匹配，


