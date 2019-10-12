from Tkinter import *
import tkFileDialog as fd

def get_file_name(file_entry):
    file_name = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
    file_entry.delete(0,END)
    file_entry.insert(0,file_name)

def run_and_close(event=None):
    ######################################
    ## EXECUTE OR CALL OTHER PYTHON FILE##
    ######################################
    close()

def close(event=None):
    root.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing

root = Tk()
root.title("1002 Project Upload CSV File")
root.state("zoomed")

entry_csv=Entry(root, text="", width=80, font=20)
entry_csv.place(x=250, y=380)
entry_csv2=Entry(root, text="", width=80, font=20)
entry_csv2.place(x=250, y=500)

Label(root,  bg="#64dd17", height=10, font=30, text="1002 Dataset Analyzer").pack(fill=X)
Label(root, text="1st Dataset File: ", font=30).place(x=100, y=380)
Button(root, text="Browse...", width=10, height=2, command=lambda:get_file_name(entry_csv)).place(x=1000, y=370)
Label(root, text="2nd Dataset File:", font=30).place(x=100, y=500)
Button(root, text="Browse...", width=10, height=2, command=lambda:get_file_name(entry_csv2)).place(x=1000, y=490)

Button(root, text="Upload",     command=run_and_close, width=10, height=2).place(x=1250, y=430)
#Button(root, text="Cancel", command=close, width=10).grid(row=3, column=2, sticky=W)

root.bind('<Return>', run_and_close)
root.bind('<Escape>', close)
mainloop()