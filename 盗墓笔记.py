
#encoding=utf-8
import requests,pymongo,threadpool,time,threading
from bs4 import BeautifulSoup
urll='http://www.quanshu.net/book/9/9055/'
lista=[]
def open_index(url):
    req=requests.get(url)
    if req.status_code == 200:
        req.encoding=req.apparent_encoding
        return req.text
    else:
        print('打开页面错误')
def parser_index(htmla):
    htmll=BeautifulSoup(htmla,'html.parser')
    finda=htmll.find_all('div',{'class':'clearfix dirconone'})
    for i in finda:
        li=i.find_all('li')
        for a_a in li:
            lista.append(a_a.a['href'])
def save(values):
    client=pymongo.MongoClient('localhost',27017)
    dbname=client['周考三']
    dataname=dbname['盗墓笔记']
    dataname.insert(values)
def parser_zi(html):
    lock.acquire()
    htmlz=BeautifulSoup(html,'html.parser')
    findtit=htmlz.find('strong',{'class':'l jieqi_title'})
    findcon=htmlz.find('div',{'id':"content"})
    content=findcon.get_text()[10:].strip()
    title=findtit.string[3:]
    lock.release()
    dict={
        'title':title,
        'content':content
    }
    save(dict)
    print('---------------------------------')
def main(llist):
    htmlzi=open_index(urll+llist)
    parser_zi(htmlzi)
if __name__ == '__main__':
    lock=threading.Lock()
    start=time.time()
    html=open_index(urll)
    parser_index(html)
    list=[x for x in lista[:20]]
    pool=threadpool.ThreadPool(20)
    str_a=threadpool.makeRequests(main,list)
    [pool.putRequest(x) for x in str_a]
    pool.wait()
    end=time.time()
    print(end-start)