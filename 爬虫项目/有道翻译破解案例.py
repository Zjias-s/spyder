import requests
import time
from hashlib import md5
import random

#获取相关加密算法结果
def get_salt_sign_ts(word):
    #ts,时间戳
    ts=str(int(time.time()*1000))
    #salt
    salt=ts+str(random.randint(0,9))
    #sign
    string="fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
    s=md5()
    s.update(string.encode())
    sign=s.hexdigest()
    
    return salt,sign,ts
    
#调用有道翻译
def attack_yd(word):
    #调用函数，得到三个会更改的值
    salt,sign,ts=get_salt_sign_ts(word)
    #F12抓包后的url地址
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers={'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Content-Length':'238',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            #检查最多的三个
            'Cookie':'OUTFOX_SEARCH_USER_ID=1112064569@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=2092445081.122926; JSESSIONID=aaacBfmuPH9Ysd3H4Bxbx; ___rl__test__cookies=1582031311224',
            'Host':'fanyi.youdao.com',
            'Origin':'http://fanyi.youdao.com',
            #从哪里跳转过来的
            'Referer':'http://fanyi.youdao.com/',
            #useragent
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'}
    data={'i':word,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'ts':ts,
        'bv':'42160534cfa82a6884077598362bbc9d',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME'}
    
    html=requests.post(url,headers=headers,data=data).json()
    translate=html["translateResult"][0][0]["tgt"]
    print(translate)
    

if __name__=='__main__':
    word=input('请输入要翻译的单词:')
    attack_yd(word)












