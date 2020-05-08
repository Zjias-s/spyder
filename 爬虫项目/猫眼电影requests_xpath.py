import requests
import time
from lxml import etree
import random

class MaoyanSpider(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        self.page=1
    
    def get_page(self,url):
        res=requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        html=res.text
        self.parse_page(html)
    
    #用xpath做数据提取
    def parse_page(self,html):
        parse_html=etree.HTML(html)
        dd_list=parse_html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
        for dd in dd_list:
            name=dd.xpath('./div/div/div[1]/p[1]/a/text()')
            if name:
                name=name[0].strip()
            else:
                name="null"
                
            star=dd.xpath('./div/div/div[1]/p[2]/text()')
            if star:
                star=star[0].strip()
            else:
                star="null"
                
            time=dd.xpath('./div/div/div[1]/p[3]/text()')
            if time:
                time=time[0].strip()[5:15]
            else:
                time="null"
            
            print(
                    {'名称':name,
                     '主演':star,
                     '时间':time}
                    )
            
        
    
    def main(self):
        for offset in range(0,21,10):
            url=self.url.format(str(offset))
            
            self.get_page(url)
            print('第%d页完成' % self.page)
            self.page+=1
            time.sleep(random.randint(1,3))
    
if __name__=='__main__':
    spider=MaoyanSpider()
    spider.main()
