import csv
import pandas as pd

with open('data.csv', 'w') as csvfile:
    
    writer = csv.writer(csvfile, delimiter=',')
    # writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['001', 'mike', 30])
    writer.writerows([['002', 'lee', '30'], ['003', 'zhang', '40']])


with open('data.csv', 'a', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
    writer.writeheader()
    writer.writerow({'id':'004', 'name': 'wang', 'age':46})
    writer.writerow({'id':'005', 'name': '彭', 'age':46})


with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)



df = pd.read_csv('data.csv')
print(df)