import csv
from datetime import datetime


def searchTenderIdNo(idNo, csv_file):
    # Creates list to store data
    tenderNo = []
    agency = []
    tenderDescription = []
    awardDate = []
    tenderDetailStatus = []
    supplierName = []
    awardedAmt = []
    
    # Opens the CSV file
    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    found = False
    
    # Iterates through the CSV file, identify the user defined Tender ID no. and store in list
    for row in reader:
        tender = row[0]
        if tender == idNo:
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

    # Determine and locate all rows that contains value defined by user
    results = df.loc[dfList.tender_no.str.contains(idCode)]

    return results


def searchDateRange(startDate, endDate):
    # Opens the CSV file and locate the award_date column
    df = pd.read_csv('government-procurement-via-gebiz.csv', parse_dates=True)
    dfList = df.loc[:, ['award_date']]
    
    # Convert the starting date and ending date into a datetime format
    dfList.award_date = pd.to_datetime(dfList.award_date)
    
    # Determine the values between two dates of a date column as user defined
    results = df.loc[(dfList.award_date > startDate) & (dfList.award_date <= endDate)]

    return results


# print searchDateRange("2015-2-5", "2015-2-7")
# print searchTenderIdCode("AGC")
# print searchTenderIdNo("AGO000ETT15000001", "government-procurement-via-gebiz.csv")

