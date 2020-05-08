import requests
import time
from lxml import etree
import random

class LianjiaSpider(object):
    def __init__(self):
        self.url='https://quanzhou.lianjia.com/ershoufang/pg{}/'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        self.page=1
    
    def get_page(self,url):
        res=requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        html=res.text
        self.parse_page(html)
    
    #用xpath做数据提取
    def parse_page(self,html):
        parse_html=etree.HTML(html)#创建解析对象re.compile("正则表达式",re.S)
        #解析对象调用xpath  r_list=p.findall('html文件')
        li_list=parse_html.xpath('//*[@id="content"]/div[1]/ul/li/div[@class="info clear"]')
        for li in li_list:
            where=li.xpath('./div[2]/div[1]/a[1]/text()')[0].strip()
            total_price=li.xpath('./div[6]/div[1]/span/text()')[0].strip()
            unit_price=li.xpath('./div[6]/div[2]/span/text()')[0].strip()
            
            print(where,total_price,unit_price)
    
    def main(self):
        for pg in range(1,3):
            url=self.url.format(str(pg))
            
            self.get_page(url)
            print('第%d页完成' % self.page)
            self.page+=1
            time.sleep(random.randint(1,3))
        
    
if __name__=='__main__':
    spider=LianjiaSpider()
    spider.main()


#'//*[@id="content"]/div[1]/ul/li/div[@class="info clear"]'
#"./div[2]/div[1]/a[1]/text()"
#"./div[6]/div[1]/span/text()"
#"./div[6]/div[2]/span/text()"


