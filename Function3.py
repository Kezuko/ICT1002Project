import csv
import datetime
import dictionary as dictionary
import pandas as pd
from numpy.core import records


def function3(csv_file):
    records = {}  # stores <agency_name> : <procurement amount>

    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    for row in reader:
        if header:
            agency = row[1]
            award_amount = float(row[6])

            if agency in records.keys():
                records[agency] += award_amount

            else:
                records[agency] = award_amount
        else:
            header = True

    f.close()

    return records


def function3Asc(csv_file):
    records = {}  # stores <agency_name> : <procurement amount>

    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    for row in reader:
        if header:
            agency = row[1]
            award_amount = float(row[6])

            if agency in records.keys():
                records[agency] += award_amount

            else:
                records[agency] = award_amount
        else:
            header = True

    f.close()

    recordAsc = sorted(records.values())

    return recordAsc


def function3Dsc(csv_file):
    records = {}  # stores <agency_name> : <procurement amount>

    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    for row in reader:
        if header:
            agency = row[1]
            award_amount = float(row[6])

            if agency in records.keys():
                records[agency] += award_amount

            else:
                records[agency] = award_amount
        else:
            header = True

    f.close()

    recordDsc = sorted(records.values(), reverse=True)

    return recordDsc


print function3("government-procurement-via-gebiz.csv") #print default list
print function3Asc("government-procurement-via-gebiz.csv") #print ascending list
print function3Dsc("government-procurement-via-gebiz.csv") #print descending list
