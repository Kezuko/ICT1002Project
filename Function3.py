import csv


def eachSectorTotalAmtProcurement(csv_file):
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


def eachSectorTotalAmtProcurementAsc(csv_file):
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


def eachSectorTotalAmtProcurementDsc(csv_file):
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


print function3("government-procurement-via-gebiz.csv") #test print default list
print function3Asc("government-procurement-via-gebiz.csv") #test print ascending list
print function3Dsc("government-procurement-via-gebiz.csv") #test print descending list
