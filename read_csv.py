import csv 

with open('data.csv','r') as f:
    csv_file = csv.reader(f)
    print(type(csv_file))

    for row in csv_file:
        print(row)

a = 1
