from fake_useragent import UserAgent
import requests
from lxml import etree
import random

class XiciSpider(object):
    def __init__(self):
        self.url='https://www.xicidaili.com/nn/'
        self.headers={'User-Agent':self.get_random_ua()}
        self.proxies_list=[]

    #获取随机UA
    def get_random_ua(self):
        ua=UserAgent()
        return ua.random

    #从西刺代理网站获取ip
    def get_ip_list(self):
        html=requests.get(self.url,headers=self.headers).text
#        print(html)
        #解析
        parse_html=etree.HTML(html)
        tr_list=parse_html.xpath('//table[@id="ip_list"]/tr')
        for tr in tr_list[1:]:
            ip=tr.xpath('./td[2]/text()')[0]
            port=tr.xpath('./td[3]/text()')[0]
            proxies={'http':'http://{}:{}'.format(ip,port),
                     'https':'https://{}:{}'.format(ip,port)}
            self.proxies_list.append(proxies)
        print(self.proxies_list)
        
        

if __name__=='__main__':
    spider=XiciSpider()
    spider.get_ip_list()
    





'//table[@id="ip_list"]/tbody/tr/td[2]/text()'
'//table[@id="ip_list"]/tbody/tr/td[3]/text()'