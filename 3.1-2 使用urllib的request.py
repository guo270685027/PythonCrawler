from urllib import request,parse
import ssl
# request1 = request.Request('http://python.org')
# # 返回Request类型的对象
# ssl._create_default_https_context = ssl._create_unverified_context
# #　 全局取消证书验证
# response = request.urlopen(request1)
# print(response.read().decode("utf-8"))

url = 'http://httpbin.org/post'
headers ={
    'User-Agent':'Mozilla/4.9 (compatible; MSIE S. S; Windows NT)',
    'Host':'httpbin.org',
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='post')
#method用大写，不然会urllib.error.HTTPError: HTTP Error 400: Bad Request，返回的类型为request类型
#req .add_header(’ User-Agent p ,’Mozilla/4 .0 (compatible; MSIE 5.5; Windows NT )’)
response = request.urlopen(req)
print(response.read().decode('utf-8'))