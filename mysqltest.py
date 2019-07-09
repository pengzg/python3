import pymysql
db = pymysql.connect(host='', user='root', password='', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database Version', data)
cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
db.close()