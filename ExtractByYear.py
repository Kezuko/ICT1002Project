import csv
import pandas as pd
import datetime


governmentcsv = pd.read_csv('government-procurement-via-gebiz.csv',parse_dates=True) #read csv and it contain dates (parse_dates = true)
extract = governmentcsv.loc[:, ['supplier_name','award_date']] #only getting these columns

extract.award_date= pd.to_datetime(extract.award_date)

#extract 2015

year_2015 = extract[(extract.award_date.dt.year == 2015)] #extract only year 2015
index_year_2015 = year_2015.reset_index(drop = True) #reset index
index_year_2015.index += 1 #and index start from 1
export_csv = year_2015.to_csv(r'C:\Users\User\Desktop\year_2015.csv') #print out in csv file
print index_year_2015
print "Save on your desktop \nFolder Name: year_2015.csv"

#extract 2016
#
year_2016 = extract[(extract.award_date.dt.year == 2016)] #extract only year 2015
index_year_2016 = year_2016.reset_index(drop = True) #reset index
index_year_2016.index += 1 #and index start from 1
export_csv = year_2016.to_csv(r'C:\Users\User\Desktop\year_2016.csv') #print out in csv file
print year_2016
print "Save on your desktop \nFolder Name: year_2016.csv"



# #extract 2017

year_2017 = extract[(extract.award_date.dt.year == 2017)] #extract only year 2015
index_year_2017 = year_2017.reset_index(drop = True) #reset index
index_year_2017.index += 1 #and index start from 1
export_csv = year_2017.to_csv(r'C:\Users\User\Desktop\year_2017.csv') #print out in csv file
print year_2017
print "Save on your desktop \nFolder Name: year_2017.csv"

# extract all not na

notNA = extract[(extract.supplier_name != 'na')] #extract only year 2015
index_notNA = notNA.reset_index(drop = True) #reset index
index_notNA.index += 1 #and index start from 1
export_csv = notNA.to_csv(r'C:\Users\User\Desktop\NotNA.csv') #print out in csv file
print notNA
print "Save on your desktop \nFolder Name: NotNA.csv"
