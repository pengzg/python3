import urllib.request
import urllib.parse
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
param = {'token':'2b82da1e1454429fa780c8bab5912627', 'recordid':'35425425425'}
data = bytes(urllib.parse.urlencode(param), encoding='utf-8')
request = urllib.request.Request('https://yxtest.sqkx.net/mobile/work/commonQueryControl/queryWaterRecordList.action', data=data, headers=headers, origin_req_host=None, method='GET')
request.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))




