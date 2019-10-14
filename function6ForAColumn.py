import collections
import csv

def comparisonForCategorization(gov, categorizeAgency):
    # Returns all the registered contractors that were awarded a tender
    # This in a in-built python function that compares the columns of data from both csv files for similar value
    similar_company = set(gov).intersection(categorizeAgency)
    # Sorts the data by alphabetical order
    reg_return = {'Registered': sorted(similar_company)}
    return reg_return

def categorization_awarded(gov, categorizeAgency, categoryValue):
    reg_awarded_return = collections.OrderedDict()
    reg = comparisonForCategorization(gov, categorizeAgency)

    for company_name in reg['Registered']:
        for supplier_name in range(len(gov)):
            if company_name == gov[supplier_name]:
                if company_name not in reg_awarded_return:
                    reg_awarded_return[company_name] = float(categoryValue[supplier_name])
                else:
                    reg_awarded_return[company_name] += float(categoryValue[supplier_name])

    return reg_awarded_return


cname = open('Categorize_Agency.csv')
# cname = open(file1)
catergorizeCSVFILE = csv.reader(cname)  # Read the data
catergorizeName = next(catergorizeCSVFILE)  # Print from the second rows onwards

gname = open('government-procurement-via-gebiz.csv')
# gname = open(file2)
supplierCSVFile = csv.reader(gname)  # read the data
supplierName = next(supplierCSVFile)  # Print from the second rows onwards


categorizeList = []
govAgencyList = []
categorizeAwardList = []


for categorize in catergorizeCSVFILE:  # Contractor File
    if categorize[0] != "":
        categorizeList.append(categorize[0][3:])  #

for govAgency in supplierCSVFile:  # Contractor File
    govAgencyList.append(govAgency[1])  #
    categorizeAwardList.append(govAgency[6])

#print comparisonForCategorization(agencyList, categorizeList)
#print categorization_awarded(govAgencyList, categorizeList, categorizeAwardList)

totalValueOfCategory = sum(categorization_awarded(govAgencyList, categorizeList, categorizeAwardList).values()) # sum of total
print totalValueOfCategory
