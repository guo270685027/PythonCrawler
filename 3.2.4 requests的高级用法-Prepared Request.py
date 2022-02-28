from requests import Request,Session

url = 'https://httpbin.org/post'
data = {
    'name':'GXL'
}
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1'
}
s = Session()
req = Request('Post',url,data=data,headers=headers)
#requests 在发送请求的时候在内部构造了一个 Request 对象
prepared = s.prepare_request(req)
#再调用 Session 的 prepare_request 方法将其转换为一个 Prepared Request 对象
r = s.send(prepared)
#调用 send 方法发送
print(r.text)

