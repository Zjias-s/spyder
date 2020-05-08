import requests
import json

class TencentSpider(object):
    def __init__(self):
        self.headers={'cookie':'_ga=GA1.2.1450021470.1570949456; pgv_pvi=8495036416; loading=agree',
                      'authority':'careers.tencent.com',
                      'method':'GET',
                      'path':'/tencentcareer/api/post/ByPostId?timestamp=1&postId=1230328965554507776&language=zh-cn',
                      'scheme':'https',
                      'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                      'accept-encoding':'gzip, deflate, br',
                      'accept-language':'zh-CN,zh;q=0.9',
                      'cache-control':'max-age=0',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        self.one_url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1582119489341&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url='https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1582168762155&postId={}&language=zh-cn'

    #获取页面
    def get_page(self,url):
        res=requests.get(url,headers=self.headers)
        html=json.loads(res.text)
        
        return html
    
    #解析一级页面
    def parse_one_page(self,html):
        for job in html['Data']['Posts']:
            job_name=job['RecruitPostName']
            post_id=job['PostId']
    
            #拼接二级页面的url地址
            two_level=self.two_url.format(post_id)
            #职责和要求
            job_duty,job_req=self.parse_two_page(two_level)
            
            d={'名称':job_name,
               '职责':job_duty,
               '要求':job_req}
            print(d)
            
    def parse_two_page(self,two_level):
        html=self.get_page(two_level)
        job_duty=html['Data']['Responsibility']
        job_req=html['Data']['Requirement']
        
        return job_duty,job_req
        
    def main(self):
        for pageindex in range(1,2):
            url=self.one_url.format(str(pageindex))
            html=self.get_page(url)
            self.parse_one_page(html)
        
        
if __name__=='__main__':
    spider=TencentSpider()
    spider.main()




#'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1582119489341&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
#'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1582123291273&postId={}&language=zh-cn'