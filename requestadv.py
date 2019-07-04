import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)

print('==============cookie=================')
r = requests.get('http://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():
    print(key+'=='+value)
