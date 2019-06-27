import urllib.request
import urllib.parse
import socket
print('1111')
response = urllib.request.urlopen("https://www.python.org")
print(response.read().decode("utf-8"))
print(type(response))
print(response.getheaders())
print(response.getheader('Server'))
print('2222')
data = bytes(urllib.parse.urlencode({'world':'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
print('3333')
#response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.001)
#print(response.read())
print('4444')
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.001)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')