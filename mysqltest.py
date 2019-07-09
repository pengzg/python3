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



# id = '20120001'
# user = 'Bob'
# age = 20
 
# db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='spiders')
# cursor = db.cursor()
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