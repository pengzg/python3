import urllib.request

request = urllib.request.Request('https://python.org', data=None, headers={}, origin_req_host=None)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
