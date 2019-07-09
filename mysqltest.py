import pymysql
host = ''
pwd = ''

# db = pymysql.connect(host=host, user='root', password=pwd, port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database Version', data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
# db.close()

# db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()


db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='spiders')
cursor = db.cursor()

# id = '20120001'
# user = 'Bob'
# age = 25
 

# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()



# db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='spiders')
# cursor = db.cursor()
# data = {
#     'id': '20120005',
#     'name': 'Bob',
#     'age': 20
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# print(sql)
# try:
#    if cursor.execute(sql, tuple(data.values())):
#        print('Successful')
#        db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()



# db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#    cursor.execute(sql, (25, 'Bob'))
#    db.commit()
# except:
#    db.rollback()
# db.close()


# db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='spiders')
# cursor = db.cursor()
# data = {
#     'id': '20120001',
#     'name': 'Bob',
#     'age': 29
# }
 
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
 
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
# update = ','.join([" {key} = %s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values())*2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()


# db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='spiders')
# cursor = db.cursor()
# table = 'students'
# condition = 'age > 20'
 
# sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     print('Successful')
#     db.commit()
# except:
#     print('Fail')
#     db.rollback()
 
# db.close()



# sql = 'SELECT * FROM students WHERE age >= 20'
 
# try:
#     cursor.execute(sql)
#     print('Count:', cursor.rowcount)
#     one = cursor.fetchone()
#     print('One:', one)
#     results = cursor.fetchall()
#     print('Results:', results)
#     print('Results Type:', type(results))
#     for row in results:
#         print(row)
# except:
#     print('Error')


sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')