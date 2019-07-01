from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit


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