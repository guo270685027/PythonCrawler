import requests
import logging
# # s =requests.Session()  #<class 'requests.sessions.Session'>
# # s.get('http://httpbin.org/cookies/set/number/123456789')
# # r = s.get('http://httpbin.org/cookies')  #<class 'requests.models.Response'>
# # print(r.text)
# # print(type(r))
# #利用Session ，可以做到模拟同一个会话而不用担心Cookies 的问题。它通常用于模拟登录成功之后再进行下一步的操作。
#
# logging.captureWarnings(True)   #忽略警告
# response= requests.get('http://www.12306.cn',verify=False)
# print(response.status_code)

# 设置代理
# proxies = {
#     'http':'http://171.92.21.39:9000',
# }
# requests.get('https://www.taobao.com',proxies=proxies)

# 超时设置
# r = requests.get('https://www.taobao.com',timeout=1)
# 实际上，请求分为两个阶段，即连接（ connect ）和读取（ read ）。上面设置的timeout将用作连接和读取这二者的timeout总和。
# 如果要分别指定，就可以传入一个元组：timeout =()
# print(r.status_code)

# 身份验证
# from requests.auth import HTTPBasicAuth
# r= requests.get('http://www.localhost:5000',auth=HTTPBasicAuth('123','456'))
#import requests
r = requests.get('http://www.localhost:5000',auth=('123','456'))

print(r.status_code)