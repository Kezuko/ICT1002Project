import csv
import pandas as pd
import datetime


governmentcsv = pd.read_csv('government-procurement-via-gebiz.csv',parse_dates=True) #read csv and it contain dates (parse_dates = true)
extract = governmentcsv.loc[:, ['supplier_name','award_date']] #only getting these columns

extract.award_date= pd.to_datetime(extract.award_date)

#extract 2015

year_2015 = extract[(extract.award_date.dt.year == 2015)] #extract only year 2015
year_2015.reset_index(drop = True,inplace=True) #reset index
year_2015.index += 1 #and index start from 1
export_csv = year_2015.to_csv(r'C:\Users\User\Desktop\year_2015.csv') #print out in csv file
print year_2015
print "Save on your desktop \nFolder Name: year_2015.csv"

#extract 2016

year_2016 = extract[(extract.award_date.dt.year == 2016)] #extract only year 2016
year_2016.reset_index(drop = True,inplace=True) #reset index
year_2016.index += 1 #and index start from 1
export_csv = year_2016.to_csv(r'C:\Users\User\Desktop\year_2016.csv') #print out in csv file
print year_2016
print "Save on your desktop \nFolder Name: year_2016.csv"



#extract 2017

year_2017 = extract[(extract.award_date.dt.year == 2017)] #extract only year 2016
year_2017.reset_index(drop = True, inplace=True) #reset index
year_2017.index += 1 #and index start from 1
export_csv = year_2017.to_csv(r'C:\Users\User\Desktop\year_2017.csv') #print out in csv file
print year_2017
print "Save on your desktop \nFolder Name: year_2017.csv"

# extract all supplier that is not na

notNA = extract[(extract.supplier_name != 'na')] #extract only year 2016
notNA.reset_index(drop = True,inplace=True) #reset index
notNA.index += 1 #and index start from 1
export_csv = notNA.to_csv(r'C:\Users\User\Desktop\NotNA.csv') #print out in csv file
print notNA
print "Save on your desktop \nFolder Name: NotNA.csv"


#supplier not na and year 2015

notNAFifteen = extract[(extract.supplier_name != 'na') & (extract.award_date.dt.year == 2015)] #extract only year 2016
notNAFifteen.reset_index(drop = True,inplace=True) #reset index
notNAFifteen.index += 1 #and index start from 1
export_csv = notNAFifteen.to_csv(r'C:\Users\User\Desktop\2015_NotNA.csv') #print out in csv file
print notNAFifteen
print "Save on your desktop \nFolder Name: 2015_NotNA.csv"


#supplier not na and year 2016

notNASixteen = extract[(extract.supplier_name != 'na') & (extract.award_date.dt.year == 2016)] #extract only year 2016
notNASixteen.reset_index(drop = True,inplace=True) #reset index
notNASixteen.index += 1 #and index start from 1
export_csv = notNASixteen.to_csv(r'C:\Users\User\Desktop\2016_NotNA.csv') #print out in csv file
print notNASixteen
print "Save on your desktop \nFolder Name: 2016_NotNA.csv"

#supplier not na and year 2017

notNASeventeen = extract[(extract.supplier_name != 'na') & (extract.award_date.dt.year == 2017)] #extract only year 2016
notNASeventeen.reset_index(drop = True,inplace=True) #reset index
notNASeventeen.index += 1 #and index start from 1
export_csv = notNASeventeen.to_csv(r'C:\Users\User\Desktop\2017_NotNA.csv') #print out in csv file
print notNASeventeen
print "Save on your desktop \nFolder Name: 2017_NotNA.csv"


