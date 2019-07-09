import csv


with open('data.csv', 'w') as csvfile:
    
    writer = csv.writer(csvfile, delimiter=',')
    # writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['001', 'mike', 30])
    writer.writerows([['002', 'lee', '30'], ['003', 'zhang', '40']])