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


def searchTenderIdNo(uniqueNo, csv_file):
    tenderNo = []
    agency = []
    tenderDescription = []
    awardDate = []
    tenderDetailStatus = []
    supplierName = []
    awardedAmt = []

    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    found = False

    for row in reader:
        tender = row[0]
        if tender == uniqueNo:
            tenderNo.append(str(row[0]))
            agency.append(str(row[1]))
            tenderDescription.append(str(row[2]))
            awardDate.append(str(row[3]))
            tenderDetailStatus.append(str(row[4]))
            supplierName.append(str(row[5]))
            awardedAmt.append(str(row[6]))
            break  # leave for loop
    else:
        found = True

    f.close()

    searchReturn = {
        "Tender No.": tenderNo,
        "Agency": agency,
        "Tender Description": tenderDescription,
        "Award Date": awardDate,
        "Tender Detail Status": tenderDetailStatus,
        "Supplier Name": supplierName,
        "Awarded Amount": awardedAmt
    }

    return searchReturn


print searchTenderIdNo("AGC000ETT14000010", "government-procurement-via-gebiz.csv") #test print search by ID
print function3("government-procurement-via-gebiz.csv") #test print default list
print function3Asc("government-procurement-via-gebiz.csv") #test print ascending list
print function3Dsc("government-procurement-via-gebiz.csv") #test print descending list
