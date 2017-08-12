import requests,os
from bs4 import BeautifulSoup

urll='https://www.lagou.com/'
req=requests.get(urll)
req.encoding=req.apparent_encoding
code=req.text
html=BeautifulSoup(code,'lxml')
finda=html.find_all('li',{'class':"position_list_item default_list"})
lista=[]
for i in finda:
    tit=i.find('div',{'class':"position_name"})
    content=i.find('div',{'class':"pli_btm_r fl wordCut"})
    gong=i.find('div',{'class':"pli_btm_l fl"})
    dd=i.find('div',{'class':"pli_btm_r fl wordCut"})
    ss=i.find('span',{'class':"wordCut"})

    title=tit.a.get_text()
    gonf=gong.get_text().strip()
    ddd=dd.get_text().strip()
    print(ddd)
    print(gonf)
    print(title)


