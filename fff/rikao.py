import requests,time,pymongo
import threadpool,threading
from bs4 import BeautifulSoup
lista= []
urll='http://www.x23us.com/html/55/55519/'
req=requests.get(urll)
req.encoding=req.apparent_encoding
code=req.text
html=BeautifulSoup(code,'lxml')
finda=html.find_all('td',{'class':"L"})
for i in finda[:-2]:
    lista.append(i.a['href'])


def cun(values):
    client=pymongo.MongoClient('localhost',27017)
    daname=client['ok']
    dadaname=daname['opp']
    dadaname.insert(values)

def open_index(url):
    open_in =requests.get(url)
    if open_in.status_code == 200:
        open_in.encoding=open_in.apparent_encoding
        return open_in.text
    else:
        print('打开网页错误')

def parser_index(parser):
    html=BeautifulSoup(parser,'lxml')
    findtit=html.find('h1')
    findta=html.find('dd',{'id':"contents"})
    title=findtit.string.strip()
    conetent=findta.get_text().strip()
    print(title+'/n'+conetent)
    dict={
        'title':title,
        'conetent':conetent
    }
    cun(dict)


def main(listt):
    lock.acquire()
    html=open_index(urll+listt)
    parser_index(html)
    lock.release()

if __name__=='__main__':
    lock=threading.Lock()
    start=time.time()
    pool=threadpool.ThreadPool(3)
    list=[x for x in lista[:6]]
    reqq=threadpool.makeRequests(main,list)
    [pool.putRequest(x) for x in reqq]
    pool.wait()
    end=time.time()
    print(end-start)



