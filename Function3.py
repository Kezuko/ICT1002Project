import collections
import csv
import operator

def eachSectorTotalAmtProcurementDefault(csv_file):
    # Stores <agency_name> : <procurement amount>
    records = {}

    # Opens the CSV file
    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    # Iterates through the CSV file, go through agency and procurement amount, and calculate total procurement
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
    # Sorts the records in no order and return result
    return records

def eachSectorTotalAmtProcurementAtoZ(csv_file):
    # Stores <agency_name> : <procurement amount>
    records = {}

    # Opens the CSV file
    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    # Iterates through the CSV file, go through agency and procurement amount, and calculate total procurement
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
    # Sorts the records in A-Z order and return result
    records = collections.OrderedDict(sorted(records.items()))
    return records

def eachSectorTotalAmtProcurementZtoA(csv_file):
    # Stores <agency_name> : <procurement amount>
    records = {}

    # Opens the CSV file
    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    # Iterates through the CSV file, go through agency and procurement amount, and calculate total procurement
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
    # Sorts the records in Z-A order and return result
    records = collections.OrderedDict(sorted(records.items(), reverse=True))
    return records

def eachSectorTotalAmtProcurementAsc(csv_file):
    # Stores <agency_name> : <procurement amount>
    records = {}

    # Opens the CSV file
    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    # Iterates through the CSV file, go through agency and procurement amount, and calculate total procurement
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
    # Sorts the records in ascending order and return result
    recordsAsc = collections.OrderedDict(sorted(records.items(), key=operator.itemgetter(1), reverse=True))
    return recordsAsc

def eachSectorTotalAmtProcurementDsc(csv_file):
    # Stores <agency_name> : <procurement amount>
    records = {}

    # Opens the CSV file
    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False
    
    # Iterates through the CSV file, go through agency and procurement amount, and calculate total procurement
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
    # Sorts the records in descending order and return result
    recordsDesc = collections.OrderedDict(sorted(records.items(), key=operator.itemgetter(1), reverse=False))
    return recordsDesc
