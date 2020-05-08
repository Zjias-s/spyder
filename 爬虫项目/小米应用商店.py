import requests
from threading import Thread
import json
from queue import Queue
import time

class XiaomiSpider(object):
    def __init__(self):
        self.url='http://app.mi.com/categotyAllListApi?page={}&categoryId=5&pageSize=30'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
        #创建队列
        self.q=Queue()
        self.i=0
        
    #URL入队列
    def url_in(self):
        for page in range(11):
            #入队列
            self.q.put(self.url.format(str(page)))
            
        
    #线程事件函数：获取队列中的URL，发请求解析处理数据
    def get_data(self):
        #获取url,做解析
        while True:
            if self.q.empty():
                break
            else:
                url=self.q.get()
                html=requests.get(url,headers=self.headers
                                  ).text
                html=json.loads(html)
                for app in html['data']:
                    app_name=app['displayName']
                    app_url=app['packageName']
                    self.i+=1
                    app_dict={'应用名称':app_name,
                              '应用链接':app_url}
                    
                    with open('xiaomi.json','a') as f:
                        json.dump(app_dict,f,ensure_ascii=False)
                
        
    def main(self):
        #入队列
        self.url_in()
        #创建多个线程并启动线程
        t_list=[]
        for i in range(5):
            t=Thread(target=self.get_data)
            t_list.append(t)
            t.start()
        #回收线程
        for i in t_list:
            i.join()
        print(self.i)
            
if __name__=='__main__':
    start=time.time()
    spider=XiaomiSpider()
    spider.main()
    end=time.time()
    print(end-start)












'http://app.mi.com/categotyAllListApi?page={}&categoryId=5&pageSize=30'
