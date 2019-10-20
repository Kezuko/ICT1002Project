import ttk
import tkinter as tk
import csv
import pandas as pd

root2 = tk.Tk()

canvas1 = tk.Canvas(root2, width=400, height=300, relief='raised')
canvas1.pack()

# -----------------------------------------------Titles/Labels---------------------------------------------------------#
label1 = tk.Label(root2, text='Open Function 3 (Search Function)')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root2, text='Please enter and select relevant submission')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

# -----------------------------------------------UserInput-------------------------------------------------------------#
userInput1 = tk.Entry(root2)
canvas1.create_window(200, 140, window=userInput1)


# -----------------------------------------------SearchByIdNo----------------------------------------------------------#
def searchTenderIdNo():
    global lstbox
    global scrollbar
    try:
        lstbox.destroy()
        scrollbar.destroy()
    except:
        print "none"

    scrollbar = ttk.Scrollbar(root2, orient=tk.HORIZONTAL)
    scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    lstbox = tk.Listbox(root2)
    lstbox.pack()
    lstbox.config(width=0)

    idNo = userInput1.get()

    tenderNo = ""
    agency = ""
    tenderDescription = ""
    awardDate = ""
    tenderDetailStatus = ""
    supplierName = ""
    awardedAmt = ""

    # Opens the CSV file
    f = open("government-procurement-via-gebiz.csv", 'rb')
    reader = csv.reader(f, delimiter=',')
    header = False

    # Iterates through the CSV file, identify the user defined Tender ID no. and store in list
    for row in reader:
        if header:
            tender_no = row[0]
            if tender_no == idNo:
                tenderNo = row[0]
                agency = row[1]
                tenderDescription = row[2]
                awardDate = row[3]
                tenderDetailStatus = row[4]
                supplierName = row[5]
                awardedAmt = row[6]
                break  # leave for loop
        else:
            header = True

    f.close()

    # Return results in the following format
    searchReturn = {
        "Tender No.": tenderNo,
        "Agency": agency,
        "Tender Description": tenderDescription,
        "Award Date": awardDate,
        "Tender Detail Status": tenderDetailStatus,
        "Supplier Name": supplierName,
        "Awarded Amount": awardedAmt
    }

    for key in searchReturn:
        lstbox.insert(tk.END, '{}: {}'.format(key, searchReturn[key]))

    lstbox.config(xscrollcommand=scrollbar.set)
    scrollbar.config(command=lstbox.xview)


# -----------------------------------------------SearchByIdCode--------------------------------------------------------#
def searchTenderIdCo():
    global lstbox
    global scrollbar
    try:
        lstbox.destroy()
        scrollbar.destroy()
    except:
        print "none"

    scrollbar = ttk.Scrollbar(root2, orient=tk.HORIZONTAL)
    scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    lstbox = tk.Listbox(root2)
    lstbox.pack()
    lstbox.config(width=0)

    idCode = userInput1.get()

    df = pd.read_csv("government-procurement-via-gebiz.csv")
    dfList = df.loc[:, ['tender_no']]

    # Determine and locate all rows that contains value defined by user
    results = df.loc[dfList.tender_no.str.contains(idCode)]

    # Adds an unique Id number column and assign to each row
    results = results.assign(id_no=[i for i in xrange(len(results))])[['id_no'] + results.columns.tolist()]

    # Return results with index set and as a dictionary
    myDR = results.set_index('id_no').T.to_dict('list')

    for key in myDR:
        lstbox.insert(tk.END, '{}: {}'.format(key, myDR[key]))

    lstbox.config(xscrollcommand=scrollbar.set)
    scrollbar.config(command=lstbox.xview)


# -----------------------------------------------SearchByIdDate--------------------------------------------------------#
def searchByDate():
    global lstbox
    global scrollbar
    try:
        lstbox.destroy()
        scrollbar.destroy()
    except:
        print "none"

    scrollbar = ttk.Scrollbar(root2, orient=tk.HORIZONTAL)
    scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    lstbox = tk.Listbox(root2)
    lstbox.pack()
    lstbox.config(width=0)

    startDate = userInput1.get()

    df = pd.read_csv("government-procurement-via-gebiz.csv", parse_dates=True)
    dfList = df.loc[:, ['award_date']]

    # Convert the starting date and ending date into a datetime format
    dfList.award_date = pd.to_datetime(dfList.award_date)

    # Determine the values between two dates of a date column as per user defined
    results = df.loc[(dfList.award_date == startDate)]

    # Add an unique Id number column and assign to each row
    results = results.assign(id_no=[i for i in xrange(len(results))])[['id_no'] + results.columns.tolist()]

    # Return results with index set and as a dictionary
    myDR = results.set_index('id_no').T.to_dict('list')

    for key in myDR:
        lstbox.insert(tk.END, '{}: {}'.format(key, myDR[key]))

    lstbox.config(xscrollcommand=scrollbar.set)
    scrollbar.config(command=lstbox.xview)


# ----------------------------------------------Buttons(Submit)--------------------------------------------------------#
button1 = tk.Button(text='Search by: Tender ID', command=searchTenderIdNo, bg='black', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(23, 180, window=button1)

button2 = tk.Button(text='Search by: Tender ID Code', command=searchTenderIdCo, bg='black', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(173, 180, window=button2)

button3 = tk.Button(text='Search by: Tender Date (YYYY-MM-DD)', command=searchByDate, bg='black', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(370, 180, window=button3)

root2.mainloop()
