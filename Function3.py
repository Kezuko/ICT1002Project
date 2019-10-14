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


def sortRecord():
    recordList = function3("government-procurement-via-gebiz.csv")

    print("Sort by ascending order enter 1")
    print("Sort by descending order enter 2")
    inpOrder = int(input("Enter a number: "))

    if inpOrder == 1:
        recordList = sorted(recordList.values())
    elif inpOrder == 2:
        recordList = sorted(recordList.values(), reverse=True)
    else:
        print("Invalid input!")

    return recordList


print sortRecord()
