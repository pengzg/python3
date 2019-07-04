import requests
import re

print("========get=======")
r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
print("========post=======")
r = requests.post('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
print("========delete=======")
r = requests.delete('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
print("========put=======")
r = requests.put('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
print("========head=======")
r = requests.head('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
print("========options=======")
r = requests.options('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)


data = {
    'name': 'lee',
    'age':22
}
r = requests.get('https://httpbin.org/get', params=data)
print(r.text)

print('==========json=============')
r = requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))

print('===============知乎===============')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore', headers = headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

print('==============抓取二进制=====================')
r = requests.get('https://github.com/favicon.ico')
print('===r.text====')
print(r.text)
print('===r.content====')
print(r.content)
print('==============wb=====================')
r = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f :
    f.write(r.content)
print('==============知乎不传headers=====================')
r = requests.get('https://www.zhihu.com/explore')
print(r.text)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
print(r.text)

print('==============POST=====================')

data = {
    'name':'lee',
    'age': '22'
}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
data = {'name': 'germey', 'age': '22'}
data = {
    'name':'lee',
    'age': '22'
}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)