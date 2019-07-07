import requests
from bs4 import BeautifulSoup
import re

offset = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90']

def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def soupmain():
    for i in offset:
        url = 'https://maoyan.com/board/4?offset='+i
        print(url)
        pageHtml = get_one_page(url)
        soup = BeautifulSoup(pageHtml,'lxml')
        news_titles = soup.select("div.board-item-main div div p a")
        for n in news_titles:
            print(n.get_text())
            
def remain():
    for i in offset:
        url = 'https://maoyan.com/board/4?offset='+i
        print(url)
        pageHtml = get_one_page(url)
        r = re.findall('<dd>.*?title="(.*?)".*?board-img.*src="(.*?)".*?star">(.*?)</p>.*?score.*?integer">(.*?)</i>.*?fraction">(.*?)</i>', pageHtml, re.S)
        #print(r)
        #print(type(r))
        for result in r:
            #print(result)
            print(result[0], result[1], result[2], result[3],result[4])

remain()