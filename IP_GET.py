import requests
from lxml import etree
import time
from collections import Iterable,Iterator

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
f = open("ip_list.txt",'w')

def ip181_daili(pages):
    for page in range(1,pages):
        url = "http://www.ip181.com/daili/{page}.html".format(page=page)
        r = requests.get(url = url,headers=headers)
        time.sleep(5)
        html = etree.HTML(r.text)
        one = html.xpath('//tbody/tr')
        one = one[1:]
        for i in one:
            ip = i.xpath('td[1]/text()')[0]
            port = i.xpath('td[2]/text()')[0]
            with open("ip_list.txt",'a') as g:
                g.write(r'http://'+ip+':'+port+'\n')
# ip181_daili(10)

def kuai_daili(pages):
    url = "https://www.kuaidaili.com/free/inha/{page}/"
    for page in range(1,pages):
        r = requests.get(url=url.format(page = page),headers=headers)
        time.sleep(3)#不设置一下会返回503的状态
        html = etree.HTML(r.text)
        print(r.status_code)
        one = html.xpath('//tbody/tr')
        for i in one:
            ip = i.xpath('td[1]/text()')[0]
            port = i.xpath('td[2]/text()')[0]
            with open("ip_list.txt",'a') as f:
                f.write('http://'+ip+":"+port+"\n")
# kuai_daili(20)
def xici_daili(pages):
    url = "http://www.xicidaili.com/nn/{page}"
    for page in range(1,pages):
        r = requests.get(url = url.format(page=page),headers=headers)
        time.sleep(5)
        print(r.status_code)
        html = etree.HTML(r.text)
        one = html.xpath('//table/tr')[1:]
        for i in one:
            ip = i.xpath('td[2]/text()')[0]
            port = i.xpath('td[3]/text()')[0]
            with open("ip_list.txt",'a') as f:
                f.write('http://'+ip+":"+port+'\n')
# xici_daili(5)

def ip66_daili(pages):
    url = "http://www.66ip.cn/{page}.html"
    for page in range(1,pages):
        r = requests.get(url = url.format(page=page),headers=headers)
        time.sleep(5)
        print(r.status_code)
        html = etree.HTML(r.text)
        one = html.xpath('//table/tr')[4:]
        # print(one)
        for i in one:
            ip = i.xpath('td[1]/text()')[0]
            port = i.xpath('td[2]/text()')[0]
            with open("ip_list.txt",'a') as f:
                f.write('http://'+ip+":"+port+"\n")
# ip66_daili(5)

ip181_daili(10)
kuai_daili(20)
xici_daili(10)
ip66_daili(10)

