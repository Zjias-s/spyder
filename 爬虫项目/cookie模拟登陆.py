import requests
from lxml import etree

#方法一，用F12抓取登陆后的cookie，发送请求到登陆后的地址，携带cookie放在headers中

#方法二
#寻找登陆时POST地址
#url='http://www.renren.com/PLogin.do'
#发送用户名和密码到POST地址
#1.先POST（把用户名和密码POST到一个地址中）
post_url='http://www.renren.com/PLogin.do'
post_data={'email':'','password':''}
headers={'Host':'www.renren.com',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
session=requests.session()
session.post(post_url,headers=headers,data=post_data)
#2.再DET（访问需要登陆后才能访问）
url='http://www.renren.com/972422958'
html=session.get(url,headers=headers).text
print(html)