import requests    #导入用于发送请求的库
import re    #导入筛选出小说内容的库
import time # 导入时间库
from bs4 import BeautifulSoup #导入BeautifulSoup库
import io
import sys

#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#小说地址，包含章节目录的信息
book_url = 'http://www.kenshuzw.info/xiaoshuo/229347/0/'

#用于后面拼接小说章节地址
base_url='http://www.kenshuzw.info'


# 模拟浏览器请求头，减少被识别为爬虫的概率
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}

# response = requests.get(url=book_url, headers=headers)
# selector = parsel.Selector(response.text)
# a = selector.xpath('//a/@href').extract()
# for i in a:
#     print(i)
#     if i.startswith('/xiaoshuo/229347/'):
#         with open('url.txt','a+',encoding="utf-8") as f:
#             f.write(i+'\n')


#以下是提取正文内容的正则表达式，是通过分析小说内容特点的源码来写的
content_regx='<br />\n&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'

#所以匹配出小说章节标题的正则表达式如下
title_regx='<h1 class="article-title">(.*?)</h1>'

#设置小说保存路径
##如果爬取的时候出现permission deny，请修改下面的sava_path,例如可以直接修改为 save_path="三寸人间.txt"
#这样以后爬取的小说会与Python文件保存在同一个路径
save_path='给不起彩礼.txt'
count=0

with open (save_path,'a+',encoding="utf-8") as f:
#从存放小说章节地址的列表中依次去除小说地址，让requests通过get方法去取货
    url_list=open('url.txt','r',encoding="utf-8").readlines()
    for url in url_list:
        #一直向小说章节所在地址发送请求并获得响应,直到响应里面没有 ”503 Service Temporarily Unavailable“
        print(url)
        time.sleep(1)
        url1=base_url+url[:-2]
        response_2=requests.get(url=url1, headers=headers)
        time.sleep(1)
        #判断响应是否正常，如果是503，则继续发送请求，直到响应正常
        print(response_2.status_code)
        if response_2.status_code==503:
            print('503')
            time.sleep(3)
            continue
        #设定编码，解决乱码
        response_2.encoding='utf-8'

        #小说标题,匹配到的是str类型
        title=re.findall(title_regx, response_2.text)
        try:
            print(title[0])
        except:
            print('no title')
            continue
        #将小说标题写入文
        f.write('------------------'+title[0]+'---------------'+'\n')
        #正文内容，匹配到的是列表
        print(count)
        count+=1
        content = re.findall(content_regx, response_2.text)
        #将小说内容这个列表中的所有元素写入文件，每写入一个就换一次行
        for e in content:
            f.write(e+'\n')
