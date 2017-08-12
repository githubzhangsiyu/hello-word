#encoding:utf-8
import requests,os
from bs4 import BeautifulSoup

class fun():#创建一个类
    def __init__(self):
        self.lista=[]#连接列表
        self.patha='E://Django4/untitled25/xpath/'#路径
    def open(self,url):#
        self.req=requests.get(url)
        self.req.encoding=self.req.apparent_encoding
        self.code=self.req.text
    def html(self,values):
        htmll=BeautifulSoup(values,'lxml')
        self.findd=htmll.find_all('img',{'width':'84'})
        self.title=htmll.find('h1')
        self.title=self.title.get_text().strip()
        for i in self.findd:
            self.lista.append(i['src'])
    def xh(self,paths,list):
        for num,a in enumerate(list):
            a_a=requests.get(a).content
            _file=open(paths+str(num)+'.jpg','wb')
            _file.write(a_a)
            _file.close()
            print('下载'+str(num)+'张')
    def start(self,url):
        self.open(url)
        self.html(self.code)
        self.patha=self.patha+self.title+'//'
        if os.path.exists(self.patha):
            print('存在了')
            os.chdir(self.patha)
            self.xh(self.patha,self.lista)
        else:
            print('创建中')
            os.makedirs(self.patha)
            self.xh(self.patha,self.lista)
url='http://esf.fang.com/chushou/3_361604373.html'
stu=fun()
stu.start(url)



