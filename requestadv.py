import requests
print('==============文件上传=================')
files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)

print('==============cookie=================')
r = requests.get('http://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():
    print(key+'=='+value)

print('==============cookie -set=================')

headers = {
    'Cookie': 'cookie: _xsrf=5o7919wNcryMmuXZYfbTGtrwHHyFzQzT; _zap=1b30aa33-f0b0-4bfe-8487-135d8c0f6190; d_c0="AMCsaA4tfw-PTmrVeF45ikSY0sw5Y_uFjT8=|1559012674"; q_c1=31a29da294074113acf38145a187c814|1559012676000|1559012676000; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330; capsion_ticket="2|1:0|10:1562232782|14:capsion_ticket|44:MmYzM2UyOGYxNjJkNGExMmJmNWU3ZTdlNGRiZWUwOWM=|f0f881609f1aa25f0feb26d5413c9a3ae1b797e385c3ca6c3cf616cf67d3d901"; z_c0="2|1:0|10:1562232816|4:z_c0|92:Mi4xT0hlU0FnQUFBQUFBd0t4b0RpMV9EeVlBQUFCZ0FsVk43eFVMWGdDYXlhZ25RTWMycC1qNGszcHJ0VHNjRXNQa1Jn|d4afbb104bad5682d271a354aabb7edcfacdbe24aa6e38ca5d72bdd79b3267d9"; unlock_ticket="ABBKvm0nbAkmAAAAYAJVTfjOHV1nxiCODdKGLS3ssbfwElX8m1ku8Q=="; tst=r',
    'Host': 'www.zhihu.com',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

r = requests.get('https://www.zhihu.com', headers = headers)
print(r.text)

print('==============cookie-jar===============')

cookies = 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
print(r.text)



cookies2 = '_xsrf=5o7919wNcryMmuXZYfbTGtrwHHyFzQzT; _zap=1b30aa33-f0b0-4bfe-8487-135d8c0f6190; d_c0="AMCsaA4tfw-PTmrVeF45ikSY0sw5Y_uFjT8=|1559012674"; q_c1=31a29da294074113acf38145a187c814|1559012676000|1559012676000; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330; capsion_ticket="2|1:0|10:1562232782|14:capsion_ticket|44:MmYzM2UyOGYxNjJkNGExMmJmNWU3ZTdlNGRiZWUwOWM=|f0f881609f1aa25f0feb26d5413c9a3ae1b797e385c3ca6c3cf616cf67d3d901"; z_c0="2|1:0|10:1562232816|4:z_c0|92:Mi4xT0hlU0FnQUFBQUFBd0t4b0RpMV9EeVlBQUFCZ0FsVk43eFVMWGdDYXlhZ25RTWMycC1qNGszcHJ0VHNjRXNQa1Jn|d4afbb104bad5682d271a354aabb7edcfacdbe24aa6e38ca5d72bdd79b3267d9"; unlock_ticket="ABBKvm0nbAkmAAAAYAJVTfjOHV1nxiCODdKGLS3ssbfwElX8m1ku8Q=="; tst=r'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
print(type(cookies2))
for cookie in cookies2.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
print(r.text)








