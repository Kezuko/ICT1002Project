import csv
import collections

# Function for registered & non-registered company
def registered(supplier, company):
    # Returns all the registered contractors that were awarded a tender
    # This in a in-built python function that compares the columns of data from both csv files for similar value
    similar_company = set(supplier).intersection(company)
    # Sorts the data by alphabetical order
    reg_return = {'Registered': sorted(similar_company)}
    return reg_return


def non_registered(supplier, company):
    # Returns all the non-registered contractors that were awarded a tender This is a in-built python function
    # Compares the columns of data from both csv files and return the value not found in the second csv file
    not_listed = set(supplier).difference(company)
    # Sort it by alphabetical order
    non_reg_return = {'Non-Registered': sorted(not_listed)}
    return non_reg_return


def registered_awarded(supplier, company, awarded):
    reg_awarded_return = collections.OrderedDict()
    reg = registered(supplier, company)

    for company_name in reg['Registered']:
        for supplier_name in range(len(supplier)):
            if company_name == supplier[supplier_name]:
                if company_name not in reg_awarded_return:
                    reg_awarded_return[company_name] = float(awarded[supplier_name])
                else:
                    reg_awarded_return[company_name] += float(awarded[supplier_name])

    return reg_awarded_return


def non_registered_awarded(supplier, company, awarded):
    non_reg_awarded_return = collections.OrderedDict()
    non_reg = non_registered(supplier, company)

    for company_name in non_reg['Non-Registered']:
        for supplier_name in range(len(supplier)):
            if company_name == supplier[supplier_name]:
                if company_name not in non_reg_awarded_return:
                    non_reg_awarded_return[company_name] = float(awarded[supplier_name])
                else:
                    non_reg_awarded_return[company_name] += float(awarded[supplier_name])

    return non_reg_awarded_return


# Old code that print list(company name) and list(value)
def sort_contractors(reg_award, non_reg_award):
    sorted_contractors = collections.OrderedDict()
    sort_contractor = []
    sort_value = []
    non_reg_award.update(reg_award)
    x = 0
    while x < 5:
        for count in sorted(non_reg_award, key=non_reg_award.get, reverse=True):
            sort_contractor.append(count)
            sort_value.append(non_reg_award[count])
            sorted_contractors = sort_contractor, sort_value
            x = x + 1
            if x >= 5:
                break
        return sorted_contractors


""" # NEW CODE THAT PRINT KEY:VALUE
def sort_contractors(reg_award, non_reg_award):
    sorted_contractors = collections.OrderedDict()
    sort_contractor = []
    sort_value = []
    non_reg_award.update(reg_award)
    x = 0
    while x < 5:
        for count in sorted(non_reg_award, key = non_reg_award.get, reverse=True):
            sort_contractor.append(count)
            sort_value.append(non_reg_award[count])
            sorted_contractors = dict(zip(sort_contractor, sort_value))
            x = x + 1
            if x >=5:
                break
        return sorted_contractors
        """

# Allow user input of file
# file1 = raw_input("Enter file:")
# file2 = raw_input("Enter file:")


cname = open('listing-of-registered-contractors.csv')
# cname = open(file1)
companyCSVFILE = csv.reader(cname)  # Read the data
companyName = next(companyCSVFILE)  # Print from the second rows onwards

gname = open('government-procurement-via-gebiz.csv')
# gname = open(file2)
supplierCSVFile = csv.reader(gname)  # read the data
supplierName = next(supplierCSVFile)  # Print from the second rows onwards

# Create empty list
companyNameList = []
supplierNameList = []
awardList = []

for allCompanyName in companyCSVFILE:  # Contractor File
    companyNameList.append(allCompanyName[0])  # Append the company names

for allSupplierName in supplierCSVFile:  # Government File
    if allSupplierName[5] != 'na':  # If supplier names is not equal to na
        supplierNameList.append(allSupplierName[5])  # Append the supplier names
        awardList.append(allSupplierName[
                             6])  # As some of the companies can have 0 value awarded, but still a company. Hence, we can't use totalAwardAmt != 0 as a condition. However, NA for companies surely means 0 for awarded amount

reg_award = registered_awarded(supplierNameList, companyNameList, awardList)
non_reg_award = non_registered_awarded(supplierNameList, companyNameList, awardList)

# print reg
# print non_reg
# print registered_awarded(supplierNameList, companyNameList, awardList)
# print non_registered_awarded(supplierNameList, companyNameList, awardList)
print sort_contractors(reg_award, non_reg_award)
