import pandas as pd

governmentcsv = pd.read_csv('government-procurement-via-gebiz.csv',parse_dates=True) #read csv and it contain dates (parse_dates = true)
extract = governmentcsv.loc[:, ['supplier_name','award_date','awarded_amt']] #only getting these columns
extract.award_date = pd.to_datetime(extract.award_date)

# ##output 2015 all without awarded_amt == 0
def year_2015_without_nan_function():
    year_2015_notNa = extract[(extract.awarded_amt != 0.0)&(extract.award_date.dt.year == 2015)]    #extract only year 2015
    year_2015_notNa_sort = year_2015_notNa.sort_values('awarded_amt',ascending =False)    #ascending = false , to output the highest amount first
    topFive_2015 = year_2015_notNa_sort.head(5)
    year_2015_notNa_index = topFive_2015.reset_index(drop = True)
    year_2015_notNa_index.index += 1  #and index start from 1
    return year_2015_notNa_index
#print year_2015_without_nan_function() #print 2015 without amt == 0

# ##output 2016 all without awarded_amt == 0
def year_2016_without_nan_function():
    year_2016_notNa = extract[(extract.awarded_amt != 0.0)&(extract.award_date.dt.year == 2016)]    #extract only year 2015
    year_2016_notNa_sort = year_2016_notNa.sort_values('awarded_amt',ascending =False)    #ascending = false , to output the highest amount first
    topFive_2016 = year_2016_notNa_sort.head(5)
    year_2016_notNa_index = topFive_2016.reset_index(drop = True)
    year_2016_notNa_index.index += 1  #and index start from 1
    return year_2016_notNa_index
#print year_2016_without_nan_function() #print 2016 without amt == 0

#
# #output 2017 all without awarded_amt == 0
def year_2017_without_nan_function():
    year_2017_notNa = extract[(extract.awarded_amt != 0.0)&(extract.award_date.dt.year == 2017)]    #extract only year 2015
    year_2017_notNa_sort = year_2017_notNa.sort_values('awarded_amt',ascending =False)    #ascending = false , to output the highest amount first
    topFive_2017 = year_2017_notNa_sort.head(5)
    year_2017_notNa_index = topFive_2017.reset_index(drop = True)
    year_2017_notNa_index.index += 1  #and index start from 1
    return year_2017_notNa_index
#print year_2017_without_nan_function() #print 2017 without amt == 0

# #output all without awarded_amt == 0
def all_without_nan_function():
    All_notNa = extract[(extract.awarded_amt != 0.0)]    #extract only year 2015
    All_notNa_amt= All_notNa.sort_values('awarded_amt',ascending =False)    #ascending = false , to output the highest amount first
    All_notNa_amt.reset_index(drop = True,inplace = True)
    All_notNa_amt.index += 1  #and index start from 1
    return All_notNa_amt
print all_without_nan_function()
