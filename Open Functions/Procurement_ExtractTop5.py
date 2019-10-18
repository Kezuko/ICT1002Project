import csv
import pandas as pd
import datetime
import collections

governmentcsv = pd.read_csv('government-procurement-via-gebiz.csv',parse_dates=True) #read csv and it contain dates (parse_dates = true)
extract = governmentcsv.loc[:, ['supplier_name','award_date','awarded_amt']] #only getting these columns
extract.award_date = pd.to_datetime(extract.award_date)
#extract 2015

def year_2015_funtion():
    year_2015 = extract[(extract.award_date.dt.year == 2015)]  #extract only year 2015
    year_2015_amt = year_2015.sort_values('awarded_amt',ascending =False)   #ascending = false , to output the highest amount first
    topFive_2015 = year_2015_amt.head(5) #getting the top 5
    year_2015_reset = topFive_2015.reset_index(drop = True)  #reset index
    year_2015_reset.index += 1  #and index start from 1
    export_csv = year_2015_reset.to_csv(r'C:\Users\User\Desktop\year_2015_top5.csv') #print out in csv file
    # print year_2015_reset
    print "Save on your desktop \nFolder Name: year_2015_top5.csv"
    return year_2015_reset

# print year_2015_funtion() #to print year 2015 top 5

#
# #extract 2016
def year_2016_funtion():
    year_2016 = extract[(extract.award_date.dt.year == 2016)] #extract only year 2015
    year_2016_sort = year_2016.sort_values('awarded_amt',ascending =False) #sort the date
    topFive_2016 = year_2016_sort.head(5)
    year_2016_index = topFive_2016.reset_index(drop = True) #reset index
    year_2016_index.index += 1 #and index start from 1
    export_csv = year_2016_index.to_csv(r'C:\Users\User\Desktop\year_2016_top5.csv') #print out in csv file
    print "Save on your desktop \nFolder Name: year_2016_top5.csv"
    return year_2016_index

# print year_2016_funtion() #to print year 2016 top 5

# # #extract 2017
def year_2017_funtion():
    year_2017 = extract[(extract.award_date.dt.year == 2017)]  #extract only year 2015
    year_2017_sort = year_2017.sort_values('awarded_amt',ascending =False) #sort the date
    topFive_2017 = year_2017_sort.head(5)
    year_2017_index = topFive_2017.reset_index(drop = True) #reset index
    year_2017_index.index += 1 #and index start from 1
    export_csv = year_2017_index.to_csv(r'C:\Users\User\Desktop\year_2017_top5.csv') #print out in csv file
    print "Save on your desktop \nFolder Name: year_2017_top5.csv"
    return year_2017_index

# print year_2017_funtion() #print top 5 2017

# ##output 2015 all without awarded_amt == 0
def year_2015_without_nan_function():
    year_2015_notNa = extract[(extract.awarded_amt != 0.0)&(extract.award_date.dt.year == 2015)]    #extract only year 2015
    year_2015_notNa_amt= year_2015_notNa.sort_values('awarded_amt',ascending =False)    #ascending = false , to output the highest amount first
    year_2015_notNa_amt.reset_index(drop = True,inplace = True)
    year_2015_notNa_amt.index += 1  #and index start from 1
    export_csv = year_2015_notNa_amt.to_csv(r'C:\Users\User\Desktop\2015_awardedAmtNotNaN.csv') #print out in csv file
    print "Save on your desktop \nFolder Name: 2015_awardedAmtNotNaN.csv"
    return year_2015_notNa_amt
# print year_2015_without_nan_function() #print 2015 without amt == 0

# ##output 2016 all without awarded_amt == 0
def year_2016_without_nan_function():
    year_2016_notNa = extract[(extract.awarded_amt != 0.0)&(extract.award_date.dt.year == 2016)]    #extract only year 2015
    year_2016_notNa_amt= year_2016_notNa.sort_values('awarded_amt',ascending =False)    #ascending = false , to output the highest amount first
    year_2016_notNa_amt.reset_index(drop = True,inplace = True)
    year_2016_notNa_amt.index += 1  #and index start from 1
    export_csv = year_2016_notNa_amt.to_csv(r'C:\Users\User\Desktop\2016_awardedAmtNotNaN.csv') #print out in csv file
    print "Save on your desktop \nFolder Name: 2016_awardedAmtNotNaN.csv"
    return year_2016_notNa_amt
# print year_2016_without_nan_function()


#
# #output 2017 all without awarded_amt == 0
def year_2017_without_nan_function():
    year_2017_notNa = extract[(extract.awarded_amt != 0.0)&(extract.award_date.dt.year == 2017)]    #extract only year 2015
    year_2017_notNa_amt= year_2017_notNa.sort_values('awarded_amt',ascending =False)    #ascending = false , to output the highest amount first
    year_2017_notNa_amt.reset_index(drop = True,inplace = True)
    year_2017_notNa_amt.index += 1  #and index start from 1
    export_csv = year_2017_notNa_amt.to_csv(r'C:\Users\User\Desktop\2017_awardedAmtNotNaN.csv') #print out in csv file
    print "Save on your desktop \nFolder Name: 2017_awardedAmtNotNaN.csv"
    return year_2017_notNa_amt
# print year_2017_without_nan_function()

# #output all without awarded_amt == 0
def all_without_nan_function():
    All_notNa = extract[(extract.awarded_amt != 0.0)]    #extract only year 2015
    All_notNa_amt= All_notNa.sort_values('awarded_amt',ascending =False)    #ascending = false , to output the highest amount first
    All_notNa_amt.reset_index(drop = True,inplace = True)
    All_notNa_amt.index += 1  #and index start from 1
    export_csv = All_notNa_amt.to_csv(r'C:\Users\User\Desktop\AllawardedAmtNotNaN.csv') #print out in csv file
    print "Save on your desktop \nFolder Name: AllawardedAmtNotNaN.csv"
    return All_notNa_amt
print all_without_nan_function()
#
