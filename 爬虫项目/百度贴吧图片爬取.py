import requests
from lxml import etree
import time

class BaiduSpider(object):
    def __init__(self):
        self.url='https://tieba.baidu.com/f?'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    
    #获取帖子链接
    def get_tlink(self,params):
        html=requests.get(self.url,params=params,headers=self.headers).text
        parse_html=etree.HTML(html)
        t_list=parse_html.xpath('//div[@class="t_con cleafix"]/div[2]/div[1]/div[1]/a/@href')
        for t in t_list:
            t_link='http://tieba.baidu.com'+t
            self.get_ilink(t_link)
    
    def get_ilink(self,t_link):
        html=requests.get(t_link,headers=self.headers).text
        parse_html=etree.HTML(html)
        i_list=parse_html.xpath('//div[@class="d_post_content_main d_post_content_firstfloor"]//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src')
        for i in i_list:
            html=requests.get(i,headers=self.headers).content
            filename=i[-10:]
            with open('./images/'+filename,'wb') as f:
                f.write(html)
                print('%sOK'%filename)
    
    #主函数（params参数）
    def main(self):
        name=input('请输入贴吧名：')
        begin=int(input('起始页：'))
        end=int(input('终止页：'))
        for page in range(begin,end+1):
            #定义查询参数
            params={'kw':name,'pn':str((page-1)*50)}
            self.get_tlink(params)
        
        
    
if __name__=='__main__':
    spider=BaiduSpider()
    spider.main()
    
    
#'//div[@class="t_con cleafix"]/div[2]/div[1]/div[1]/a/@href'
#'//div[@class="d_post_content_main d_post_content_firstfloor"]//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src'
