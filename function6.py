def function6(csv_file1='government-procurement-via-gebiz.csv', csv_file2='Categorize_Agency.csv'):
    """Returns a dictionary in this format {<agency_name1> : <amount_spent1> , <agency_name2> : <amount_spent2> , .....}
        Amount spent is not rounded off"""

    
    records = {} #stores <agency_name> : <procurement amount>
    categorize_agency_spending = {} #categorises the agency's spending
    categorize_agency_list = [] #stores agency names
    
    f1 = open(csv_file1,'rb')
    reader1 = csv.reader(f1, delimiter=',')
    header = False

    for row in reader1:
        if header:
            agency = row[1]
            award_amount = float(row[6])

            if agency in records.keys():
                records[agency] += award_amount

            else:
                records[agency] = award_amount
        else:
            header = True

    f1.close()


    #open csv_file2 and looks for the agency in the records dictionary and adds the amount to categorize_agency_spending dictionary
    f2 = open(csv_file2,'rb')
    reader2 = csv.reader(f2, delimiter=',')
    header = False


    for row in reader2:
        column_index = 0
        if header:
            for i in row:
                if i == "":
                    column_index += 1
                    continue
                else:
                    
                    agency = i
                    agency = agency.split(".")
                    name = agency[1]
                    categorize_agency_spending[categorize_agency_list[column_index]] += records[name]
                    column_index += 1
                    
                    
                    
                    

        else:
            header = True
            for i in row:
                categorize_agency_spending[i] = 0
                categorize_agency_list.append(i)
            


    f2.close()
    return categorize_agency_spending
