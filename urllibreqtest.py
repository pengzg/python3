import urllib.request
import urllib.parse

param = {'token':'2b82da1e1454429fa780c8bab5912627'}
data = bytes(urllib.parse.urlencode(param), encoding='utf-8')
request = urllib.request.Request('https://yxtest.sqkx.net/mobile/work/commonQueryControl/queryWaterRecordList.action', data=data, headers={}, origin_req_host=None)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))


