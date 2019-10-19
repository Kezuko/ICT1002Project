import csv
from datetime import datetime


def searchTenderIdNo(idNo, csv_file):
    # Creates list to store data
    tenderNo = ""
    agency = ""
    tenderDescription = ""
    awardDate = ""
    tenderDetailStatus = ""
    supplierName = ""
    awardedAmt = ""

    # Opens the CSV file
    f = open("government-procurement-via-gebiz.csv", 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    # Iterates through the CSV file, identify the user defined Tender ID no. and store in list
    for row in reader:
        if header:
            tender_no = row[0]
            if tender_no == idNo:
                tenderNo = row[0]
                agency = row[1]
                tenderDescription = row[2]
                awardDate = row[3]
                tenderDetailStatus = row[4]
                supplierName = row[5]
                awardedAmt = row[6]
                break  # leave for loop

        else:
            header = True

    f.close()

    # Return results in the following format
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


def searchTenderIdCode(idCode):
    # Opens the CSV file and locate the tender_no column
    df = pd.read_csv('government-procurement-via-gebiz.csv')
    dfList = df.loc[:, ['tender_no']]

    # Determine and  locate all rows that contains value defined by user
    results = df.loc[dfList.tender_no.str.contains(idCode)]
    # results.index = [x for x in range(1, len(results.values) + 1)]
    # results.index.name = 'id_no'
    # Add an unique Id number column and assign to each row
    results = results.assign(id_no=[i for i in xrange(len(results))])[['id_no'] + results.columns.tolist()]
    
    # Return results with index set and as a dictionary
    myDR = results.set_index('id_no').T.to_dict('list')
    return myDR


def searchDateRange(startDate, endDate):
    # Opens the CSV file and locate the award_date column
    df = pd.read_csv('government-procurement-via-gebiz.csv', parse_dates=True)
    dfList = df.loc[:, ['award_date']]

    # Convert the starting date and ending date into a datetime format
    dfList.award_date = pd.to_datetime(dfList.award_date)

    # Determine the values between two dates of a date column as per user defined
    results = df.loc[(dfList.award_date > startDate) & (dfList.award_date <= endDate)]
    
    # Add an unique Id number column and assign to each row
    results = results.assign(id_no=[i for i in xrange(len(results))])[['id_no'] + results.columns.tolist()]
    
    # Return results with index set and as a dictionary
    myDF = results.set_index('id_no').T.to_dict('list')
    return myDF


# print searchDateRange("2015-02-04", "2015-02-06")
# print searchTenderIdCode("AGC")
# print searchTenderIdNo("AGO000ETT15000001", "government-procurement-via-gebiz.csv")

