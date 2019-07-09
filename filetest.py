import requests
from pyquery import PyQuery as pq 

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
def filew2(items):
    with open('explore.txt', 'a', encoding='utf-8') as file:
        for item in items:
            question = item.find('h2').text()
            author = item.find('.author-link-line').text()
            answer = pq(item.find('.content').html()).text()
            # 文件写入1
            #file = open('explore.txt', 'a', encoding='utf-8')
            #file.write('\n'.join([question, author, answer]))
            #file.write('\n'+ '=' * 50 + '\n')
            # 文件写入2
        
            file.write('\n'.join([question, author, answer]))
            file.write('\n'+ '='*50+'\n')

def filew(items):  
    for item in items:
            question = item.find('h2').text()
            author = item.find('.author-link-line').text()
            answer = pq(item.find('.content').html()).text()
            # 文件写入1
            file = open('explore.txt', 'a', encoding='utf-8')
            file.write('\n'.join([question, author, answer]))
            file.write('\n'+ '=' * 50 + '\n')
            file.close()

filew(items)