import pandas as pd
import collections


governmentcsv = pd.read_csv('government-procurement-via-gebiz.csv',parse_dates=True) #read csv and it contain dates (parse_dates = true)
extract = governmentcsv.loc[:, ['supplier_name','award_date']] #only getting these columns

extract.award_date= pd.to_datetime(extract.award_date)

# # # extract all supplier that is not na
def extract_supplier_not_na():
    notNA = extract[(extract.supplier_name != 'na')] #extract only year 2016
    notNA.reset_index(drop = True,inplace=True) #reset index
    notNA.index += 1 #and index start from 1
    return notNA
#print extract_supplier_not_na()

# # #supplier not na and year 2015
def extract_supplier_not_na_2015():
    notNAFifteen = dict(zip(extract['supplier_name'], extract.loc[extract.award_date.dt.year == 2015, 'award_date']))

    return notNAFifteen
#print extract_supplier_not_na_2015()


# # #supplier not na and year 2016
def extract_supplier_not_na_2016():
    notNASixteen = dict(zip(extract['supplier_name'], extract.loc[extract.award_date.dt.year == 2016, 'award_date']))

    return notNASixteen
#print extract_supplier_not_na_2016()

#
# # #supplier not na and year 2017
def extract_supplier_not_na_2017():
    notNASeventeen = dict(zip(extract['supplier_name'], extract.loc[extract.award_date.dt.year == 2017, 'award_date']))

    return notNASeventeen
#print extract_supplier_not_na_2017()

#
# #
