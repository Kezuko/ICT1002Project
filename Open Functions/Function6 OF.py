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

def open_function1(csv_file1='government-procurement-via-gebiz.csv', csv_file2='Categorize_Agency.csv'):
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
        sb_list = generate_sb_list()
        dd_list = generate_dd_list()
        
        #Temporary Menu
        print "Press '1' or '2' to select category"
        print "1. SB"
        print "2. DD"
        choice = raw_input()

        if choice == '1':
            #Temporary menu
            print "Select from the list of SB"
            for i in range(len(sb_list)):
                print str(i+1) + " " + sb_list[i]

            choice = raw_input()
            print "Spending by {0} is: {1}".format(sb_list[int(choice)-1], records[sb_list[int(choice)-1]])

        elif choice == '2':
            #Temporary menu
            print "Select from the list of DD"
            for i in range(len(dd_list)):
                print str(i+1) + " " + dd_list[i]

            choice = raw_input()
            print "Spending by {0} is: {1}".format(dd_list[int(choice)-1], records[dd_list[int(choice)-1]])
            
