import urllib.request
import csv
import time
import re

class MaoyanSpider(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    
    def get_page(self,url):
        req=urllib.request.Request(url,headers=self.headers)
        res=urllib.request.urlopen(req)
        html=res.read().decode('utf-8')
        self.parse_page(html)
    
    def parse_page(self,html):
        p=re.compile('<div class="movie-item-info">.*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        film_list=p.findall(html)
        print(film_list)
        self.write_csv(film_list)
        
    def write_csv(self,film_list):
        with open('maoyanfilm.csv','a',newline='') as f:
            writer=csv.writer(f)
            for film in film_list:
                L=[film[0].strip(),
                   film[1].strip(),
                   film[2].strip()]
                writer.writerow(L)
    
    def main(self):
        self.get_page('https://maoyan.com/board/4?offset=10')
    
if __name__=='__main__':
    spider=MaoyanSpider()
    spider.main()
    













