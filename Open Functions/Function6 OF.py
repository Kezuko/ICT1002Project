import csv

def generate_all_spending_records(csv_file='government-procurement-via-gebiz.csv'):
    """Returns a dictionary that stores each individual department and branch with amount spent
        e.g. {<name> : <amount_spent>}"""

    records = {} #stores <agency_name> : <procurement amount>
    f = open(csv_file,'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    for row in reader:
        if header:
            agency = row[1]
            award_amount = float(row[6])

            if agency in records.keys():
                records[agency] += award_amount

            else:
                records[agency] = award_amount
        else:
            header = True

    f.close()
    return records

def generate_sb_list(csv_file='Categorize_Agency.csv'):
    """Returns a list of SB"""
    sb_list = []
    
    f = open(csv_file,'rb')
    reader = csv.reader(f, delimiter=',')
    header = False
 
    for row in reader:
        column_index = 0
        if header:
            for i in row:
                if i == "":
                    column_index += 1
                    continue
                else:
                    agency = i
                    if agency[:2] == "SB":
                        agency = agency.split(".")
                        name = agency[1]
                        sb_list.append(name)
        else:
            header = True

    f.close()
    return sb_list

def generate_dd_list(csv_file='Categorize_Agency.csv'):
    """Returns a list of dd"""
    dd_list = []
    
    f = open(csv_file,'rb')
    reader = csv.reader(f, delimiter=',')
    header = False
    
    for row in reader:
        column_index = 0
        if header:
            for i in row:
                if i == "":
                    column_index += 1
                    continue
                else:
                    agency = i
                    if agency[:2] == "DD":
                        agency = agency.split(".")
                        name = agency[1]
                        dd_list.append(name)                  
        else:
            header = True
    
    return dd_list

def eachDDSBspending(csv_file1='government-procurement-via-gebiz.csv', csv_file2='Categorize_Agency.csv'):
    """Takes in raw_input() from user to view DB/SS/Total spendings
        Calls generate__all_spending_records() to generate a records dictionary
        Calls generate_sb_list()
        Calls generate_dd_list()"""
        
    #Temporary Menu
    print "Select option from menu"
    print"-------------------------"
    print "1. View SB total spending"
    print "2. View DD total spending"
    print "3. View individual DD/SB spend how much"

    choice = raw_input()
    
    records = generate_all_spending_records()
    
    if choice == "1":
        result = 0
        sb_list = generate_sb_list()
        for i in sb_list:
            result += records[i]
        print "Total SB Spending: " + str(result)
    elif choice == "2":
        result = 0
        dd_list = generate_dd_list()
        for i in dd_list:
            result += records[i]

        print "Total DD Spending: " + str(result)


    elif choice == "3":
        type = 'DD' #change this to either DD or SB
        if type == 'DD':
            lst = generate_dd_list()
        else:
            lst = generate_sb_list()
            
       for i in lst:
            print i.ljust(150) + str(records[i])
            
