import http.cookiejar, urllib.request
isfile = True
if (isfile):
    filename = 'cookie.txt'
    #cookie = http.cookiejar.MozillaCookieJar(filename)
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)
else :
    cookie = http.cookiejar.CookieJar()

    handler = urllib.request.HTTPCookieProcessor(cookie)

    opener = urllib.request.build_opener(handler)

    response = opener.open('https://www.baidu.com')
    for item in cookie:
        print(item.name+'='+item.value)
