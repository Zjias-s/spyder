import requests
import time
import random
import string


class BilibiliVideoSpider(object):
    def __init__(self):
        self.url='https://api.vc.bilibili.com/board/v1/ranking/top?'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        self.all_chars=string.punctuation + string.whitespace
        
    #获取json响应
    def get_json(self):
        for offset in range(1,12,10):
            params={'page_size':'10',
                    'next_offset':str(offset),
                    'tag':'今日热门',
                    'platform':'pc'}
            html=requests.get(self.url,params=params,
                              headers=self.headers).json()
            self.downloader(html)

    #下载视频
    def downloader(self,html):
        for video in html['data']['items']:
            video_link=video['item']['video_playurl']
            video_name=video['item']['description']
            #发请求保存视频
            for char in video_name:
                if char in self.all_chars:
                    filename=video_name.replace(char,'')
            filename=filename+'.mp4'
            
            video_content=requests.get(video_link,
                                       headers=self.headers).content
            
                                       
            with open('./video/'+filename,'wb') as f:
                f.write(video_content)
                print('%s下载成功' % filename)
                
            time.sleep(random.randint(2,5))
    
    
    
if __name__=='__main__':
    spider=BilibiliVideoSpider()
    spider.get_json()
    




























'https://vc.bilibili.com/p/eden/rank#/?tab=%E5%85%A8%E9%83%A8'