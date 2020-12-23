import csv

with open('./CarData.csv', newline='') as csv_file:
    my_reader = csv.reader(csv_file)
    for row in my_reader:
        print(row)


contenido = [['nombre', 'edad', 'sexo'], ['Juan', 18, 'M'], ['Maria', 25, 'F'], ['Irene', 15, 'F']]
with open('./csv_creado.csv', 'w', newline='') as wcsv_file:
    my_writer = csv.writer(wcsv_file)
    my_writer.writerows(contenido)

with open('./num.txt') as f:
    a = f.readline().split(',')
    print(int(a[0]) + int(a[1]))

