__author__ = 'bsbfo'
#coding=utf8
import requests
import json
from bs4 import BeautifulSoup
import json
from time import sleep
from random import randint
class ctodoudou(object):
    """登录并领取积分"""
    def __init__(self,uname,passwd):
        self.uname=uname
        self.passwd=passwd

    def login_51cto(self):
        s=requests.Session()
        login_url='http://home.51cto.com/index'
        content=s.get('http://home.51cto.com/home').content
        #获取csrf token
        soup = BeautifulSoup(content,"lxml")
        token=soup.find('meta',attrs = {'name' : 'csrf-token'})['content']
        #print (token)
        header={
            'Connection': 'keep-alive',
            'Host': 'home.51cto.com',
            'Origin': 'http://home.51cto.com',
            'Referer':'http://home.51cto.com/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        }
        data={
            '_csrf':token,
            'LoginForm[username]':self.uname,
            'LoginForm[password]': self.passwd,
            'LoginForm[rememberMe]': '0',
            'login-button': '登 录'
            }
        #模拟POST 51cto 登陆
        s.post(url=login_url,headers=header,data=data)
        #print (result.url)
        # 利用保持的Session打开主页获取登录信息
        result=s.get('http://home.51cto.com/home').text
        if self.uname in result:
            print ('恭喜,登陆51cto成功,领取下载豆中..')
        #利用保持的Session领取下载豆
        download=s.post('http://down.51cto.com/download.php?do=getfreecredits&t=0.8367867217711695').text


        if '2' in download.split(',')[1]:
            print ('领取成功,当前下载豆:'+download.split(',')[0])
        elif '1' in download.split(',')[0]:
            print ('抱歉,今天已经领取,请明天再来,当前下载豆:')
            print (download)
        else:
            print ('请注意,领取失败')
def getuserinfo():
    f=open('/data/job/config.txt','r')
    q=f.readlines()
    for i in range(len(q)):
        q[i]=q[i].strip()
    return q[0],q[1]
if __name__=="__main__":
    waittime=randint(0,500)
    print('wait '+str(waittime)+' seconds')
    sleep(waittime)
    uname,passwd=getuserinfo()
    doudou=ctodoudou(uname,passwd)
    doudou.login_51cto()
