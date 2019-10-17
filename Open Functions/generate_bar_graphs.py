from function2 import *
import pandas as pd
import operator
import matplotlib.pyplot as plt

def generate_bar_graphs(csv_file1='government-procurement-via-gebiz.csv', csv_file2='Categorize_Agency.csv'):

      #Temporary Menu
    print "Select option from menu"
    print"-------------------------"
    print "1. View SB bar graph"
    print "2. View DD bar graph"
    print "3. View all DD/SB bar graph"

    choice = raw_input()
    
    records = generate_all_spending_records()
    TOP = 10 #change this integer to change top amount of spending
    
    
    if choice == "1":
        x = generate_sb_list()
        y = []
        d = {}
        for i in records:
            if i in x:
                y.append(records[i])

        for i in range(len(x)):
            d[x[i]] = y[i]

        sorted_d = sorted(d.items(), key=operator.itemgetter(1))[::-1] #descending order
        x = []
        y = []
        print sorted_d
        for i in sorted_d:
            x.append(i[0])
            y.append(i[1])
                    

        
        data = {'x':x, 'Award Amount':y}
        df = pd.DataFrame(data)
        df = df.head(TOP)
        
        df.plot.barh(x='x', y='Award Amount', colormap='Paired')
        plt.title('Top {0} SB Award Amount'.format(TOP))
        
        
        plt.show()
        
        
        



    elif choice == "2":
        x = generate_dd_list()
        y = []
        d = {}
        for i in records:
            if i in x:
                y.append(records[i])

        for i in range(len(x)):
            d[x[i]] = y[i]

        sorted_d = sorted(d.items(), key=operator.itemgetter(1))[::-1] #descending order
        x = []
        y = []
        
        for i in sorted_d:
            x.append(i[0])
            y.append(i[1])

            
        

        
        data = {'x':x, 'Award Amount':y}
        df = pd.DataFrame(data)
        df = df.head(TOP)
        
        df.plot.barh(x='x', y='Award Amount', colormap='Paired')
        plt.title('Top {0} DD Award Amount'.format(TOP))
        
        
        plt.show()
        


    elif choice == "3":
        x = generate_sb_list() + generate_dd_list()
        y = []
        d = {}
        for i in records:
            if i in x:
                y.append(records[i])

        for i in range(len(x)):
            d[x[i]] = y[i]

        sorted_d = sorted(d.items(), key=operator.itemgetter(1))[::-1] #descending order
        x = []
        y = []

        for i in sorted_d:
            x.append(i[0])
            y.append(i[1])

            
        

        
        data = {'x':x, 'Award Amount':y}
        df = pd.DataFrame(data)
        df = df.head(TOP)
        
        df.plot.barh(x='x', y='Award Amount', colormap='Paired')
        plt.title('Top {0} DD/SB Award Amount'.format(TOP))
        
        
        plt.show()
              


    
    

     



        
        
        
       
