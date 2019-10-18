from Tkinter import *
import tkFileDialog as fd
from tkinter.messagebox import showinfo
#import Function2


def get_procurement_file(file_entry):
    file_name = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
    entry_file = file_name.split("/")[-1]
    if entry_file == "government-procurement-via-gebiz.csv":
        popup_successinfo()
        file_entry.delete(0, END)
        file_entry.insert(0, entry_file)
    else:
        popup_errorinfo()
        file_entry.delete(0, END)
    #file_entry.delete(0,END)
    #file_entry.insert(0,file_name)

def get_contractor_file(file_entry):
    file_name = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
    entry_file = file_name.split("/")[-1]
    if entry_file == "listing-of-registered-contractors.csv":
        popup_successinfo()
        file_entry.delete(0, END)
        file_entry.insert(0, entry_file)
    else:
        popup_errorinfo()
        file_entry.delete(0, END)
    #file_entry.delete(0,END)
    #file_entry.insert(0,file_name)


def popup_successinfo():
    showinfo("Window", "Successfully input!")

def popup_errorinfo():
    showinfo("Window", "Wrong input! Please insert the Correct File!")

def uploadFunction(event=None):
        print "wtf"
    #    entryTesting = entry_csv.get()
    #    entryTesting = entryTesting.split("/")[-1]
    #    Function2.function2(entryTesting)


def close(event=None):
    root.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing

root = Tk()
root.title("1002 Project Upload CSV File")
root.state("zoomed")

procurement_entry=Entry(root, text="", width=80, font=20)
procurement_entry.place(x=250, y=380)
contractor_entry=Entry(root, text="", width=80, font=20)
contractor_entry.place(x=250, y=500)

Label(root,  bg="#64dd17", height=10, font=30, text="1002 Dataset Analyzer").pack(fill=X)
Label(root, text="Procurement File: ", font=30).place(x=50, y=380)
Button(root, text="Browse...", width=10, height=2, command=lambda:get_procurement_file(procurement_entry)).place(x=1000, y=370)
Label(root, text="Contractor/Listed File:", font=30).place(x=50, y=500)
Button(root, text="Browse...", width=10, height=2, command=lambda:get_contractor_file(contractor_entry)).place(x=1000, y=490)
Button(root, text="Upload", command=uploadFunction, width=10, height=2).place(x=1250, y=430)
#Button(root, text="Cancel", command=close, width=10).grid(row=3, column=2, sticky=W)

root.bind('<Return>', uploadFunction)
root.bind('<Escape>', close)
mainloop()
