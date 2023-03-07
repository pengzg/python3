import requests
from bs4 import BeautifulSoup
import re
import urllib2 
import pymysql

host = '47.100.10.38'
pwd = 'bO96kS1vWsCmh84z'
db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='spiders')
cursor = db.cursor()
# sql = 'DROP TABLE IF EXISTS `maoyan`;CREATE TABLE IF NOT EXISTS maoyan (id VARCHAR(255) NOT NULL, name VARCHAR(255),releasetime VARCHAR(255),  stars VARCHAR(255) , img VARCHAR(255) ,point VARCHAR(255), fraction VARCHAR(255), PRIMARY KEY (id))'
# cursor.execute(sql)
sql = 'truncate table maoyan'
cursor.execute(sql)
#db.close()

offset = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90']
#offset = ['0']

def get_one_page(url):
    response = requests.get(url)
    print(response)
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
        print(pageHtml)
        # r = re.findall('<dd>.*<img.*board-img.*src="(.*)".*>.*p.*name">.*a.*>(.*)</p>.*p.*star">(.*)</p>.*releasetime">(.*)</p>.*score.*integer">(.*)</i>.*fraction">(.*)</i>', pageHtml, re.S)
        r = re.findall('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</.*?star.*?>(.*?)</.*?releasetime.*?>(.*?)</.*?integer.*?>(.*?)</.*?fraction.*?>(.*?)</.*?</dd>', pageHtml, re.S)
        print(r)
        #print(type(r))
        for result in r:
            #print(result)
            #print(result[0], result[1], result[2], result[3],result[4], result[5])
            print(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
            sql = 'INSERT INTO maoyan(id, img, name, stars, releasetime, point, fraction ) values(%s, %s, %s, %s, %s, %s,%s)'
            try:
                cursor.execute(sql, (result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
                db.commit()
            except:
                db.rollback()
    db.close()
remain()