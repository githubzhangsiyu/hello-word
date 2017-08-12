# import requests
# from bs4 import BeautifulSoup
# lista=[]
#
#
# for i in range(0,100):
#     urll='https://www.qiushibaike.com/8hr/page/'+ str(i)
#     lista.append(urll)
#
#
# for j in lista[0:10]:
#     html=requests.get(j)
#     html.encoding=html.apparent_encoding
#     code=html.text
#     coup=BeautifulSoup(code,'lxml')
#     finda=coup.find_all('div',{'class':"article block untagged mb15 typs_recent"})
#
#
#     for i in finda:
#         yu=i.find('div',{'class':"content"})
#         yuu=i.find('h2')
#         print('作者------------------------'+yuu.string.strip())
#         print('打印的内容-------------------'+yu.get_text().strip())

import threading, time


class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name  = name

    def run(self):
        time.sleep(1)  # 确保先运行Seeker中的方法
        self.cond.acquire()  # b
        print(self.name + ': 我已经把眼睛蒙上了')
        self.cond.notify()
        self.cond.wait()  # c
        print(self.name + ': 我找到你了 ~_~')
        self.cond.notify()
        self.cond.release()
        print(self.name + ': 我赢了')  # h


class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()  # a    #释放对琐的占用，同时线程挂起在这里，直到被notify并重新占有琐。
        print(self.name + ': 我已经藏好了，你快来找我吧')
        self.cond.notify()
        self.cond.wait()  # e
        self.cond.release()
        print(self.name + ': 被你找到了，哎~~~')


cond = threading.Condition()
seeker = Seeker(cond, 'seeker')
hider = Hider(cond, 'hider')
seeker.start()
hider.start()




