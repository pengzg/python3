import requests
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




