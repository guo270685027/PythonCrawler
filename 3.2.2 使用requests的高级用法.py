# 文件上传
import requests
# files = {
#     'file':open('1.ico','rb')
# }
# r = requests.post('http://httpbin.org/post',files=files)
# print(r.text)
# 获取Cookies
# r= requests.get('http://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)


# headers ={
#     'Cookie':'_zap=12ebaf2e-d111-45cd-af40-a5c572199918; d_c0="ANAd58IX-BKPTmF7OXjFMMGR-blUHkAOmhU=|1618666872"; __snaker__id=2mhFKPPd5XWISBMP; _9755xjdesxxd_=32; YD00517437729195:WM_TID=mnUzJICLKUhBBVFAFBYrgOwBVkVpkA5B; _xsrf=dglhr7Jh0bK9VYyDqu88nRS3pAi7Pfjt; gdxidpyhxdE=nBj83D71sgres2+/SV6Ssm2lZ96cqpU8IqWzKXUOCDnydRUni1EpaXDYzlV8sYbxL4LEKW8x+7M6Ig\ky6lLDfyO7RiwBWZYD3xGX1QtGLPtpVXBQZYBfT6Z0YhAx5zY+q4qNBnN5HlPiEKzvvZJ4VumKADfjscu5NQMdirnRvlhpMAY:1638456614510; YD00517437729195:WM_NI=9hKHwl9ZaamY4jwgvd9jyrpXKjoMXEwdVqR4cmIaTbDPOtBWmvImgUPz655ZmgP3dyQhm2r+vV/MWB7pfaMReqPTW3aegET5qXEFpD+EiaT4Nfpv4Ayxr+HIpDZ5sCajNlA=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eedacb5283b28dafdb5ea29a8fb6d45b969b9bbbf180ababab99ef3b8fbf8b96d02af0fea7c3b92afbb885a9f668fb86af82f053f8b6b988f570fbb6b793f35489b6a1aedb4fb5bc9a92d140a1b38782d76a88908195c15dafaa878ee65f94a6fad6b852afb9a0d4e77393b8a3d3f121b68ae1aed64af5b0aa82d05aa7afa0b5d639a3bba9a6d73fb3888ba7f350e99ba782d7408ebac097b74bbba8becccb43b49c96d6f249a3b6828dc437e2a3; z_c0=Mi4xLW16N0F3QUFBQUFBMEIzbndoZjRFaGNBQUFCaEFsVk5zQ2VXWWdDQ1dRV1o4RFF3UEoyYTlaMVF3UkcyUWs3MDh3|1638455728|739a26da84bfcd5315b7f143273bc042404f1f16; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1642329200,1642426280,1642511614,1642512086; NOT_UNREGISTER_WAITING=1; JOID=W1AXBk59Fwe_putCHHEKUg9i8LcFTClF9vqaf0xFQ2qNlbMEbofI5tKr4E8bM9QkMLJRC0clQc8jKW8jTvNbH5c=; osd=WlEQAkx8FgC7pOpDG3UIUw5l9LUETS5B9PubeEhHQmuKkbEFb4DM5NOq50sZMtUjNLBQCkAhQ84iLmshT_JcG5U=; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1642517292; SESSIONID=QtROPSdWpuueo7M5EVvxe5sDmvjXqKjXaoJyBDUtZ8x; KLBRSID=c450def82e5863a200934bb67541d696|1642517293|1642516993',
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
#     'Host':'www.zhihu.com'
# }
# r = requests.get('https://www.zhihu.com',headers=headers)
# print(r.text)


# cookies ='_zap=12ebaf2e-d111-45cd-af40-a5c572199918; d_c0="ANAd58IX-BKPTmF7OXjFMMGR-blUHkAOmhU=|1618666872"; __snaker__id=2mhFKPPd5XWISBMP; _9755xjdesxxd_=32; YD00517437729195:WM_TID=mnUzJICLKUhBBVFAFBYrgOwBVkVpkA5B; _xsrf=dglhr7Jh0bK9VYyDqu88nRS3pAi7Pfjt; gdxidpyhxdE=nBj83D71sgres2+/SV6Ssm2lZ96cqpU8IqWzKXUOCDnydRUni1EpaXDYzlV8sYbxL4LEKW8x+7M6Ig\ky6lLDfyO7RiwBWZYD3xGX1QtGLPtpVXBQZYBfT6Z0YhAx5zY+q4qNBnN5HlPiEKzvvZJ4VumKADfjscu5NQMdirnRvlhpMAY:1638456614510; YD00517437729195:WM_NI=9hKHwl9ZaamY4jwgvd9jyrpXKjoMXEwdVqR4cmIaTbDPOtBWmvImgUPz655ZmgP3dyQhm2r+vV/MWB7pfaMReqPTW3aegET5qXEFpD+EiaT4Nfpv4Ayxr+HIpDZ5sCajNlA=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eedacb5283b28dafdb5ea29a8fb6d45b969b9bbbf180ababab99ef3b8fbf8b96d02af0fea7c3b92afbb885a9f668fb86af82f053f8b6b988f570fbb6b793f35489b6a1aedb4fb5bc9a92d140a1b38782d76a88908195c15dafaa878ee65f94a6fad6b852afb9a0d4e77393b8a3d3f121b68ae1aed64af5b0aa82d05aa7afa0b5d639a3bba9a6d73fb3888ba7f350e99ba782d7408ebac097b74bbba8becccb43b49c96d6f249a3b6828dc437e2a3; z_c0=Mi4xLW16N0F3QUFBQUFBMEIzbndoZjRFaGNBQUFCaEFsVk5zQ2VXWWdDQ1dRV1o4RFF3UEoyYTlaMVF3UkcyUWs3MDh3|1638455728|739a26da84bfcd5315b7f143273bc042404f1f16; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1642329200,1642426280,1642511614,1642512086; NOT_UNREGISTER_WAITING=1; JOID=W1AXBk59Fwe_putCHHEKUg9i8LcFTClF9vqaf0xFQ2qNlbMEbofI5tKr4E8bM9QkMLJRC0clQc8jKW8jTvNbH5c=; osd=WlEQAkx8FgC7pOpDG3UIUw5l9LUETS5B9PubeEhHQmuKkbEFb4DM5NOq50sZMtUjNLBQCkAhQ84iLmshT_JcG5U=; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1642517292; SESSIONID=QtROPSdWpuueo7M5EVvxe5sDmvjXqKjXaoJyBDUtZ8x; KLBRSID=c450def82e5863a200934bb67541d696|1642517293|1642516993'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
#     'host':'www.zhihu.com'
# }
# for cookie in cookies.split(';'):
#     key,value = cookie.split('=',1)
#     jar.set(key,value)
# r =requests.get('http://www.zhihu.com',cookies=jar,headers=headers)
# print(r.text)
# 这里我们首先新建了一个RequestCookieJar 对象，然后将复制下来的cookies 利用split （）方法
# 分剖，接着利用set （）方法设置好每个Cookie 的key 和value ，然后通过调用requests 的get （）方法并
# 传递给cookies 参数即可。当然，由于知乎本身的限制， headers 参数也不能少，只不过不需要在原来的headers 参数里面设置cookie 字段了
#