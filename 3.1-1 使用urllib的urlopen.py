import urllib.request
import urllib.parse
import urllib.error
import socket

response = urllib.request.urlopen('http://www.python.org')
# HTTPResponse类型的对象
print(response.read().decode('utf-8'))
print(response.status)
# status是属性，可以得到返回结果的状态码，200 代表请求成功， 404 代表网页未找到
print(response.getheaders())
# getheaders()方法获取响应头信息，getheader()方法获取头信息里传递值的对应值
print(response.getheader("Content-Length"))
# 利用最基本的 urlopen （）方法，可以完成最基本的简单网页的 GET 请求抓取

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# 其中转字节流采用了 bytes （）方法，该方法的第一个参数需要是 str （字符串）类型
# 需要用 urllib.parse模块里的urlencode()方法来将字典转换为字符串（str），第二个参数encoding为指定编码格式
response2 = urllib.request.urlopen('http://httpbin.org/post',data=data)
# data参数需要传输bytes类型数据，加了这个参数，请求方式为POST
print(response2.read())
# word:hello在输出的form字段里，表明是模拟了表单提交的方式，以POST方式提交
try:
    response3 = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
    # timeout设置超时时间，超出时间抛出异常，不指定使用全局默认时间。
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("TIME OUT")
