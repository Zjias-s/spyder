import urllib.request
import urllib.parse
import time

class BaiduSpider(object):
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
    
    #获取页面
    def get_page(self,url):
        req=urllib.request.Request(url,headers=self.headers)
        res=urllib.request.urlopen(req)
        html=res.read().decode('utf-8')
        
        return html
    #解析页面
    def parse_page(self):
        pass
    #保存数据
    def write_page(self,filename,html):
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)
    #主函数
    def main(self):
        kw=input('请输入你要爬取的贴吧：')
        start=int(input('请输入你要爬取的起始页：'))
        end=int(input('请输入你要爬取的终止页：'))
#        kw=urllib.parse.urlencode({'kw':kw})
        #发请求保存数据
        for i in range(start,end+1):
            pn=(i-1)*50
            query_string=urllib.parse.urlencode({'kw':kw,'pn':str(pn)})
            url='http://tieba.baidu.com/f?{}'.format(query_string)
            html=self.get_page(url)
            filename='{}-第{}页.html'.format(kw,i)
            self.write_page(filename,html)
            print('第%d页爬取成功'%i)
            time.sleep(1)
        
    
if __name__=='__main__':
    spider=BaiduSpider()
    spider.main()
    
    
    