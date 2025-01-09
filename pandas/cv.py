import csv

with open('pandas/Book1.csv', 'r') as csvfile:
    csvz_reader = csv.reader(csvfile)
    for line in csvz_reader:
        print(line)