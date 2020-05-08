from selenium import webdriver
import time 


class JdSpider(object):
    def __init__(self):
        self.url='http://www.jd.com/'
        # 创建浏览器对象
        self.browser=webdriver.Chrome()
        self.i=0
        
    def get_page(self):
        self.browser.get(self.url)
        text=self.browser.find_element_by_id('key').send_keys('口罩')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)
        
    #提取商品信息
    def parse_page(self):
        #执行js脚本，把进度条拉到最底部
        self.browser.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(2)
        
        li_list=self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            product_list=li.text.split('\n')
            if product_list[0]=='<':
                price=product_list[2]
                name=product_list[3]
                market=product_list[5]
            else:
                price=product_list[0]
                name=product_list[1]
                market=product_list[3]
            print(price,name,market)
            self.i+=1
#            print(li.text)
            print('*'*50)
        print(self.i)
        
    def main(self):
        self.get_page()
        while True:
            self.parse_page()
            #判断是否点击下一页
            num=self.browser.page_source.find('pn-next disabled')
            if num == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(1)
            else:
                break
        
            
if __name__=='__main__':
    spider=JdSpider()
    spider.main()
    
    