
from redis import StrictRedis

host = ''
pwd = ''

redis = StrictRedis(host=host, port=6379, db=3, password=pwd)
redis.set('name', 'Bob')
print(redis.get('name'))
