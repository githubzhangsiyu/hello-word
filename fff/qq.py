import requests
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        r =requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('success')
        return r.text
    except:
        print('false')
        return 'false'



