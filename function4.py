import csv
import collections

# Below are 2 function (registered & non_registered) to verify whether if the company is registered or not registered
# Function for verifying company name in government csv file DOES exists in the listing contractor csv file

def reg_company(supplierList, companyList):
    similar_company = set(supplierList).intersection(companyList)  # find common company names between supplier and company
    register_company = sorted(similar_company)  # Sort the company by alphabetical order
    return register_company

# Function for verifying company name in government csv file DOES NOT exists in the listing contractor csv file
def nonreg_company(supplierList, companyList):
    non_similar_company = set(supplierList).difference(companyList)  # find non-common company names between supplier and company
    non_register_company = sorted(non_similar_company)  # Sort the company by alphabetical order
    return non_register_company

# Below are 2 function to show how much registered and not registered company were awarded
# Function to print what is the total amount each registered company was awarded
def reg_company_awardAtoZ(supplierList, companyList, awardList):
    register_award = {}
    register_company = reg_company(supplierList, companyList)

    for company_name in register_company:
        for supplier_name in range(len(supplierList)):
            if company_name == supplierList[supplier_name]:
                if company_name not in register_award:
                    register_award[company_name] = float(awardList[supplier_name])
                else:
                    register_award[company_name] += float(awardList[supplier_name])

    ascAlphaRegister_award = collections.OrderedDict(sorted(register_award.items()))
    return ascAlphaRegister_award

def reg_company_awardZtoA(supplierList, companyList, awardList):
    register_award = {}
    register_company = reg_company(supplierList, companyList)

    for company_name in register_company:
        for supplier_name in range(len(supplierList)):
            if company_name == supplierList[supplier_name]:
                if company_name not in register_award:
                    register_award[company_name] = float(awardList[supplier_name])
                else:
                    register_award[company_name] += float(awardList[supplier_name])

    descAlphaRegister_award = collections.OrderedDict(sorted(register_award.items(), reverse=True))
    return descAlphaRegister_award

# Function to print what is the total amount each non-registered company was awarded
def nonreg_company_awardAtoZ(supplierList, companyList, awardList):
    non_register_awarded = {}
    non_register_company = nonreg_company(supplierList, companyList)

    for company_name in non_register_company:
        for supplier_name in range(len(supplierList)):
            if company_name == supplierList[supplier_name]:
                if company_name not in non_register_awarded:
                    non_register_awarded[company_name] = float(awardList[supplier_name])
                else:
                    non_register_awarded[company_name] += float(awardList[supplier_name])

    ascAlphaNon_register_awarded = collections.OrderedDict(sorted(non_register_awarded.items()))
    return ascAlphaNon_register_awarded

def nonreg_company_awardZtoA(supplierList, companyList, awardList):
    non_register_awarded = {}
    non_register_company = nonreg_company(supplierList, companyList)

    for company_name in non_register_company:
        for supplier_name in range(len(supplierList)):
            if company_name == supplierList[supplier_name]:
                if company_name not in non_register_awarded:
                    non_register_awarded[company_name] = float(awardList[supplier_name])
                else:
                    non_register_awarded[company_name] += float(awardList[supplier_name])

    descAlphaNon_register_awarded = collections.OrderedDict(sorted(non_register_awarded.items(), reverse=True))
    return descAlphaNon_register_awarded

# Function to print the top 5 company by the awarded amount --> FUNCTION 5 
def top5_company(reg_award, nonreg_award):
    #top5_companies = collections.OrderedDict()
    top5_companies = []
    sort_company = []
    sort_amount = []
    nonreg_award.update(reg_award)
    x = 0
    while x < 5:
        for count in sorted(nonreg_award, key=nonreg_award.get, reverse=True):
            sort_company.append(count)
            sort_amount.append(nonreg_award[count])
            top5_companies = collections.OrderedDict(zip(sort_company, sort_amount))
            #top5_companies = sorted(dict(zip(sort_company, sort_amount)).values(), reverse=True)
            x = x + 1
            if x >=5:
                break

        return top5_companies


# Open function 4/5 - sort the register/non-register company by highest to lowest OR lowest to highest awarded amount
def sort_high_amt(high_reg):
    # Return a list that show the registered/non-registered (based on the list input) company name and it's awarded amount from highest to the lowest
    sort_company = []
    sort_amount = []
    sorted_high_value = collections.OrderedDict()

    for count in sorted(high_reg, key=high_reg.get, reverse=True):  # Sort by descending order
        sort_company.append(count)
        sort_amount.append(high_reg[count])
        sorted_high_value = zip(sort_company, sort_amount)

    return sorted_high_value


def sort_low_amt(low_reg):
    #Return a list that show the registered/non-registered (based on the list input) company name and it's awarded amount from lowest to the highest
    sort_company = []
    sort_amount = []
    sorted_low_value = collections.OrderedDict()

    for count in sorted(low_reg, key=low_reg.get, reverse=False):  # Sort by ascending order
        sort_company.append(count)
        sort_amount.append(low_reg[count])
        sorted_low_value = zip(sort_company, sort_amount)

    return sorted_low_value

# function to store only the year into a list
def dates(dateList):
    list_year = []
    for count in dateList:  # Checking the dates found in the government csv
        if count[0:4] not in list_year: # date are stored in the format yy/mm/dd, so count[0:4] will only check for the year
            list_year.append(count[0:4])  # if the year does not exist in the list called list_year, store the year.
    return list_year


# Sort registered awarded company via year
def reg_yr_award(supplierList, companyList, awardList, dateList):
    sort_years = {}
    register_company = reg_company(supplierList, companyList)  # Get the list of registered company
    years = dates(dateList) # Get the list of year (2015, 2016, 2017)
    for year in years:
        sort_award = collections.OrderedDict()
        for company_name in register_company:
            for supplier_name in range(len(supplierList)):
                if company_name == supplierList[supplier_name]:  # company_name is equal to the value of the key in the dictionary "supplierList"
                    if year in dateList[supplier_name]:
                        if year not in sort_years:
                            if company_name not in sort_award:
                                sort_award[company_name] = float(awardList[supplier_name])
                            else:
                                sort_award[company_name] += float(awardList[supplier_name])
        sort_years[year] = sort_award
    return sort_years


# Sort non-registered awarded company via year
def nonreg_yr_award(supplierList, companyList, awardList, dateList):
    sort_year = collections.OrderedDict()
    non_register_company = nonreg_company(supplierList, companyList)  # Get the list of non-registered company
    years = dates(dateList)  # Get the list of year (2015, 2016, 2017)
    for year in years:
        sort_award = collections.OrderedDict()
        for company_name in non_register_company:
            for supplier_name in range(len(supplierList)):
                if company_name == supplierList[supplier_name]:
                    if year in dateList[supplier_name]:
                        if year not in sort_year:
                            if company_name not in sort_award:
                                sort_award[company_name] = float(awardList[supplier_name])
                            else:
                                sort_award[company_name] += float(awardList[supplier_name])
        sort_year[year] = sort_award
    return sort_year

# Allow user input of csv file
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
date = []

for allCompanyName in companyCSVFILE:  # Contractor File
    companyNameList.append(allCompanyName[0])  # Append the company names which is on column 0 into the companyNameList

for allSupplierName in supplierCSVFile:  # Government File
    date.append(allSupplierName[3])
    if allSupplierName[5] != 'na':  # If supplier names is not equal to 'na'
        supplierNameList.append(allSupplierName[5])  # Append the supplier names which is on column 5 into the supplierNameList
        awardList.append(allSupplierName[6])  # As some of the companies can have 0 value awarded, but still a company. Hence, we can't use totalAwardAmt != 0 as a condition. However, NA for companies surely means 0 for awarded amount

reg_award = reg_company_awardAtoZ(supplierNameList, companyNameList, awardList)
nonreg_award = nonreg_company_awardAtoZ(supplierNameList, companyNameList, awardList)
reg = reg_company(supplierNameList, companyNameList)
nonreg = nonreg_company(supplierNameList, companyNameList)

#print reg_company
#print asc_reg_company_award
#print desc_nonreg_company_award(supplierNameList, companyNameList, awardList)
#print non_reg_award
#print reg_company(supplierNameList, companyNameList)
#print nonreg_company(supplierNameList, companyNameList)
#print reg_company_award(supplierNameList, companyNameList, awardList)
#print sort_high_amt(reg_award) # sort by highest to lowest amount of registered company
#print sort_low_amt(reg_award) # sort by lowest to highest amount of registered company
#print sort_high_amt(nonreg) # sort by highest to lowest amount of non-registered company
#print sort_low_amt(nonreg) # sort by lowest to highest amount of non-registered company
#print nonreg_company_award(supplierNameList, companyNameList, awardList)
#print top5_company_senior(reg_award, non_reg_award)
#print top5_company(reg_award, non_reg_award)

print reg_yr_award(supplierNameList, companyNameList ,awardList, date)
