from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote


result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)


result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https', allow_fragments=False)
result = urlparse('www.testdev.sqkx.net//mobile/storeApp/storeAppStoreControl/updateStoreState.action?storeid=100001181108162705187491223&box_state=1&onlinestate=2&reqCode=1002&deviceType=android&device=1&storecode=A3170004&app_version=85&bs_devicecode=f0cd23a771d3914d&fault_type=0&bs_activestate=1&appSource=4&appId=ANDROIDAPP4#comment', scheme='https', allow_fragments=False)
print(result)

result = urlparse('www.baidu.com/index.html#comment', scheme='https', allow_fragments=False)
print(result)


data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[0])

data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))

print(urljoin('https://www.baidu.com', 'FAQ.hmtl'))

params = {
    'name':'li',
    'age':22
}

base_url = 'https://www.baidu.com?'
url = base_url+urlencode(params)
print(url)

query = 'name=li&age=22'
print(parse_qs(query))
print(parse_qsl(query))


keyword = '壁纸'
url = 'https://www.baidu.com/s?wd='+quote(keyword)
print(url)

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))