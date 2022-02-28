# -*- coding: utf-8 -*-
# @Time    : 2022/1/23 10:05
# @Author  : GXL
# @FileName: 3.3.4 爬取猫眼电影排行.py
# @Software: PyCharm
import json
import re,requests
import time


def get_one_page(url):
    headers ={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    }
    res = requests.get(url,headers=headers)
    if res.status_code ==200:
        return res.text
    return None

def parse_one_page(html):
    pattern =re.compile('<div class="pic">.*?<em.*?>(.*?)</em>.*?<span.*?>(.*?)</span>',re.S)
    results =re.findall(pattern,html)
    for item in results:
        yield {
            'rank':item[0],
            'name':item[1]
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offect):
    url ='https://movie.douban.com/top250?start='+str(offect)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__=='__main__':
    for i in range(10):
        main(offect=i*25)
        time.sleep(1)