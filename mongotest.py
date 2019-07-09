import pymongo
#import bsons


#export PATH=/usr/local/mongodb/bin:$PATH
host = ''
client = pymongo.MongoClient(host=host, port=27017)
print(client)
db = client.test
collection = db.students
student = {
    'id': '20170107',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
r = collection.insert(student)
print(r)
student1 = {
    'id': '20170104',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
 
student2 = {
    'id': '20170206',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
r = collection.insert([student1, student2])
print(r)
student = {
    'id': '20170107',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
r = collection.insert_one(student)
print(r)
student1 = {
    'id': '20170104',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
 
student2 = {
    'id': '20170206',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
r = collection.insert_many([student1, student2])
print(r)
print(r.inserted_ids)


r = collection.find_one({'name':'Mike'})
print(type(r))
print(r)

# r = collection.find_one({'_id': ObjectId('5d24553091e5e73e5c2386e5')})
# print(r)




