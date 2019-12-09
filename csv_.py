import csv

mydict =[
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}]


with open('/home/alex/my/projects/lesson3/users.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']

    writer = csv.DictWriter(f, fields, delimiter=',')

    writer.writeheader()

    for user in mydict:
        writer.writerow(user)    