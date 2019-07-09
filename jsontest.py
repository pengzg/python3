import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))

print(data[0].get('age'))
print(data[0].get('age', 25))

str = '''
[{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
'''
#print(json.loads(str))

with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w') as file:
    file.write(json.dumps(data))
    file.write(json.dumps(data, indent=2))





