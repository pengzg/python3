import pymongo

#export PATH=/usr/local/mongodb/bin:$PATH
host = ''
client = pymongo.MongoClient(host=host, port=27017)
print(client)