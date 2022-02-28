import requests
#
data = {
     'name':'germey',
     'age':22
}
# r2= requests.post("http://httpbin.org/post",data=data)
r= requests.get("http://httpbin.org/get",params=data)
# print(type(r))
# print(r.status_code)
# print(r.text)
print(type(r.text))
print(r.cookies)
print(r.json())
import requests
r =requests.get('https://github.com/favicon.ico')
exit() if not r.status_code ==requests.codes.ok else print("连接成功")
with open('1.ico','wb') as f:
#open （）方法，它的第一个参数是文件名称，第二个参数代表以二进制写的形式打开
    f.write(r.content)