import csv


def eachSectorTotalAmtProcurement(csv_file):
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
    recordAsc = sorted(records.values())
    return recordAsc


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
    recordDsc = sorted(records.values(), reverse=True)
    return recordDsc

# Test print results of function
# print function3("government-procurement-via-gebiz.csv")
# print function3Asc("government-procurement-via-gebiz.csv") 
# print function3Dsc("government-procurement-via-gebiz.csv") 
