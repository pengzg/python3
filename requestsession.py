import requests
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1
from requests import Request, Session

requests.get('http://httpbin.org/cookies/set/number/12345678')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/12345678')
r = s.get('http://httpbin.org/cookies')
print(r.text)

r = requests.get('https://www.12306.cn')
print(r.status_code)

urllib3.disable_warnings()
r = requests.get('https://www.12306.cn', verify = False)
print(r.status_code)

 
proxies = {
  "http": "http://47.100.10.38:9200",
  "https": "http://47.100.10.38:80",
}
 
#r = requests.get("https://www.taobao.com", proxies=proxies)
print(r.text)
print('===================user-password======================')
proxies = {
    'http': 'http://user:password@47.100.10.38:9200'
}
#r  =requests.get('https://www.taobao.com', proxies=proxies)
print(r.text)

print('===================socks======================')
proxies = {
    'http':'socks5://user:password@host:port',
    'https':'socks5://user:password@host:port'
}
#r = requests.get('https://www.taobao.com', proxies = proxies)
print(r.text)

print('======================timeout==========================')
r = requests.get('https://www.taobao.com', timeout = 1)
print(r.status_code)

print('======================timeout(1,3,5)==========================')
r =  requests.get('https://www.taobao.com', timeout = (3, 5))
print (r.text)

print('======================timeout = None ==========================')
r = requests.get('https://www.taobao.com', timeout = None)
print(r.text)

print('====================== HTTPBasicAUTH ==========================')
#r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)

print('============================OAuth1======================================')
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
#auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
#requests.get(url, auth=auth)

print('========================Prepared Request============================')
url = 'http://httpbin.org/post'
data = {
    'name':'germey'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

s = Session()
req = Request('POST', url, data = data, headers = headers)
prepared = s.prepare_request(req)
r = s.send(prepared)
print(r.text)
