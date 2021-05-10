import csv
def reading_money():
    with open('money.txt', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            return float(row[0])


def writing_money(value):
    with open('money.txt', 'w') as csv_file:
        csv_file.write(value)
