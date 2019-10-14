import os
import csv
import datetime



class Record:
    def __init__(self):
        self.TenderNumber = ""
        self.Agency = ""
        self.TenderDescription = ""
        self.AwardDate = ""
        self.TenderStatus = ""
        self.SupplierName = ""
        self.AwardAmount = ""
        self.SerialNumber = 0
        







def function2(csv_file):
    """Reads the government agency csv files ONLY"""

    
    f = open(csv_file, 'rb')
    
    folders = [] #stores all unique agency names
    records = {} #stores key as agency_name and value as list of Record objects e.g. {<agency_name> : <[Record(), Record(), ...]>} 
    
    reader = csv.reader(f, delimiter=',')
    header = False

    #iterates through the CSV and appends unique agency names to folders
    for row in reader:
        if header:
            agency = row[1]
            if agency not in folders:
                folders.append(row[1])
        else:
            header = True
        


    f.close()

    #Creates the directory with the csv file and date as the folder name
    current_date = datetime.date.today()
    current_time = datetime.datetime.now()
    hour = str(current_time.hour)
    minute = str(current_time.minute)
    second = str(current_time.second)
        
    main_folder_name = csv_file[:-4] + "_" + str(current_date) + "_" + hour + "-" + minute + "-" + second

   
    for folder in folders:
        os.makedirs(main_folder_name + '/' + folder)
               
    
    #Opens the CSV file and puts each row into a Record object
    f = open(csv_file,'rb')
    reader = csv.reader(f, delimiter=',')
    header = False
    sn = 1
    for row in reader:
        if header:
            record = Record()
            record.TenderNumber = row[0]
            record.Agency = row[1]
            record.TenderDescription = row[2]
            record.AwardDate = row[3]
            record.TenderStatus = row[4]
            record.SupplierName = row[5]
            record.AwardAmount = row[6]
            record.SerialNumber = sn
            sn += 1

            if record.Agency in records.keys():
                records[record.Agency].append(record)

            else:
                records[record.Agency] = [record]
        else:
            header = True

    f.close()





    #Iterates through records dictionary and writes each agency's record list into the text file
    
    for key in records.keys():
        lst = records[key]
        f = open(main_folder_name + '/' + key + '/' + key + '.txt','w')
        rn = 1
        for record in lst:
            line = 'Record Number'.ljust(50) + " : " + str(rn) + '\n' \
                   + 'Tender Number'.ljust(50) + " : " + record.TenderNumber + '\n' \
                   + 'Agency'.ljust(50) + " : " + record.Agency + '\n' \
                   + 'Tender Description'.ljust(50) + " : " + record.TenderDescription + '\n' \
                   + 'Award Date'.ljust(50) + " : " + record.AwardDate + '\n' \
                   + 'Tender Status'.ljust(50) + " : " + record.TenderStatus + '\n' \
                   + 'Supplier Name'.ljust(50) + " : " + record.SupplierName + '\n' \
                   + 'Award Amount'.ljust(50) + " : " + record.AwardAmount + '\n' \
                   + 'Serial Number'.ljust(50) + " : " + str(record.SerialNumber) + '\n\n\n\n'
            rn += 1
            f.write(line)

        f.close()
