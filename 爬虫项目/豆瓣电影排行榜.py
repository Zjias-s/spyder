import requests

class DoubanSpider(object):
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        self.url='https://movie.douban.com/j/chart/top_list?'
    
    def get_page(self,params):
        res=requests.get(self.url,headers=self.headers,params=params,verify=False)#会报警告
        html=res.json()
        self.parse_page(html)
    
    def parse_page(self,html):
        for film in html:
            name=film["title"]
            score=film["score"]
            
            print({'name':name,'score':score})
    
    def main(self):
        n=input('请输入电影数量:')
        params={'type':'11',
                'interval_id':'100:90',
                'action':'',
                'start':'0',
                'limit':n}
        self.get_page(params)
        
if __name__=='__main__':
    spider=DoubanSpider()
    spider.main()
    
    
    
    
    
    
    
    
    

