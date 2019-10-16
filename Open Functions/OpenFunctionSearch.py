import csv


def searchTenderIdNo(idNo, csv_file):
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


def searchTenderIdCode(idCode, csv_file):
    myList = []
    f = open(csv_file, 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    for row in reader:
        if idCode in row[0]:
            myList.append(row)

    else:
        header = True

    f.close()

    return myList


print searchTenderIdNo("AGO000ETT15000001", "government-procurement-via-gebiz.csv")
print searchTenderIdCode("AVA", "government-procurement-via-gebiz.csv")
