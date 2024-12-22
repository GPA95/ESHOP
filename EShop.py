'''IP Project 26-07-2022'''
'''
R19028A
2R0Y1A9N
Rayyan Ali
1A7H8D2K
Ammaar Ahmad Khan'''
'''29-12-2022'''

import pandas as pd
import numpy as np
import mysql.connector as SQL

#Establishing the connectin using connect() method
C=SQL.connect(host='localhost',user='root',passwd='AAKSQL',database='EShop')
if C.is_connected():
    print('Connection secured.')
else:
    print('Could not connect.')

#Creating a cursor object using cursor() method
c=C.cursor()
print("Hello there!")
print("Welcome to EShop, our internet-based shopping platform.")
print()
print("Are you a customer(C) or a staff member(S)?")
U=str(input()).upper()
                
if U=='C':
    print("Greetings, dear customer.")
    def customer():
        chk='Y'
        while chk=='Y':
            print("Our departments:")
            Q1='SELECT * FROM DEPARTMENTS ORDER BY DeptCode'
            c.execute(Q1)
            data1=c.fetchall()
            print('Code\t Name')
            print('=======================')
            for x in data1:
                print(x[0],'\t',x[1])
                print('-----------------------')
            B=str(input("Select a department by entering its code: ")).upper()
            if B=='D001':
                print('Welcome to our electronics department.')
                print('Our products are listed below:')
                print()
                Q2='SELECT * FROM Electronics'
                c.execute(Q2)
                data2=list(c.fetchall())
                for x in data2:
                    print('Product No:',x[0])
                    print('Company:   ',x[1])
                    print('Model:     ',x[2])
                    print('Category:  ',x[3])
                    print('Price:     ',x[4])
                    print()
                P = int(input('Select the product you wish to buy by entering its number: '))
                print()
                n=int(input('How many do you want?' ))
                Colours=[]
                for x in range(n):
                    colour=str(input('Choose the colour of the item: '))
                    Colours.append(colour)
                print()
                print('The details of your chosen product are given below.')
                print()
                for x in data2:
                    if P==x[0]:
                        print('Product No:  ',x[0])
                        print('Company:     ',x[1])
                        print('Model:       ',x[2])
                        print('Category:    ',x[3])
                        print('Price/Item:  ',x[4])
                        Price=x[4]
                        TotalPrice=Price*n
                        print('Colour(s):   ',Colours)
                        print('Total price: ',TotalPrice)
                        print()
                        print('Do you confirm details of the product you wish to buy? (Y/N)')
                        _C=str(input()).upper()
                        if _C=='Y':
                            print('Please enter your following necessary details:')
                            N=str(input('Name: '))
                            P=int(input('Contact number: '))
                            E=str(input('Email address: '))
                            Ad=str(input('Address of delivery: '))
                            M=str(input('Would you like to pay through cash(C) or online(O)? ')).upper()
                            print("Amount to be paid:",TotalPrice)
                            if M=='C':
                                print('Please pay',TotalPrice,'to the deliverer of the goods.')
                            elif M=='O':
                                card=int(input('Enter your payment card number: '))
                                print('Transaction Successful.')
                            print('The item(s) shall be delivered within 48 hours at',Ad,'.')
                            print('We shall keep you updated of the shipment of the goods on your contact number',P,'and email address',E,'.')
                            print('Thank you for shopping with us,',N,'. We hope to see you soon.')
                        elif _C=='N':
                            print('Dropped')
            elif B=='D002':
                print('Welcome to our stationery department.')
                print('Our products are listed below:')
                print()
                Q2='SELECT * FROM Stationery'
                c.execute(Q2)
                data2=list(c.fetchall())
                for x in data2:
                    print('Product No:',x[0])
                    print('Brand:     ',x[1])
                    print('Item:      ',x[2])
                    print('Price:     ',x[3])
                    print()
                P = int(input('Select the product you wish to buy by entering its number: '))
                print()
                n=int(input('How many do you want?' ))
                Colours=[]
                for x in range(n):
                    colour=str(input('Choose the colour of the item: '))
                    Colours.append(colour)
                print()
                print('The details of your chosen product are given below.')
                print()                
                for x in data2:
                    if P==x[0]:
                        print('Product No:',x[0])
                        print('Brand:     ',x[1])
                        print('Item:      ',x[2])
                        print('Price/Item:',x[3])
                        Price=x[3]
                        TotalPrice=Price*n
                        print('Colour(s): ',Colours)
                        print('Total price:',TotalPrice)
                        print()
                        print('Do you confirm details of the product you wish to buy? (Y/N)')
                        _C=str(input()).upper()
                        if _C=='Y':
                            print('Please enter your following necessary details:')
                            N=str(input('Name: '))
                            P=int(input('Contact number: '))
                            E=str(input('Email address: '))
                            Ad=str(input('Address of delivery: '))
                            M=str(input('Would you like to pay through cash(C) or online(O)? ')).upper()
                            print("Amount to be paid:",TotalPrice)
                            if M=='C':
                                print('Please pay',TotalPrice,'to the deliverer of the goods.')
                            elif M=='O':
                                card=int(input('Enter your payment card number: '))
                                print('Transaction Successful.')
                            print('The item(s) shall be delivered within 48 hours at',Ad,'.')
                            print('We shall keep you updated of the shipment of the goods on your contact number',P,'and email address',E,'.')
                            print('Thank you for shopping with us,',N,'. We hope to see you soon.')
                        elif _C=='N':
                            print('Dropped')
            elif B=='D003':
                print('Welcome to our toys department.')
                print('Our products are listed below:')
                print()
                Q2='SELECT * FROM Toys'
                c.execute(Q2)
                data2=list(c.fetchall())
                for x in data2:
                    print('Product No:',x[0])
                    print('Brand:     ',x[1])
                    print('Item:      ',x[2])
                    print('Category:  ',x[3])
                    print('Price:     ',x[4])
                    print()
                P = int(input('Select the product you wish to buy by entering its number: '))
                print()
                n=int(input('How many do you want?' ))
                print()
                print('The details of your chosen product are given below.')
                print()
                for x in data2:
                    if P==x[0]:
                        print('Product No:',x[0])
                        print('Brand:     ',x[1])
                        print('Item:      ',x[2])
                        print('Category:  ',x[3])
                        print('Price/Item:  ',x[4])
                        Price=x[4]
                        TotalPrice=Price*n
                        print('Total price: ',TotalPrice)
                        print()
                        print('Do you confirm details of the product you wish to buy? (Y/N)')
                        _C=str(input()).upper()
                        if _C=='Y':
                            print('Please enter your following necessary details:')
                            N=str(input('Name: '))
                            P=int(input('Contact number: '))
                            E=str(input('Email address: '))
                            Ad=str(input('Address of delivery: '))
                            M=str(input('Would you like to pay through cash(C) or online(O)? ')).upper()
                            print("Amount to be paid:",TotalPrice)
                            if M=='C':
                                print('Please pay',TotalPrice,'to the deliverer of the goods.')
                            elif M=='O':
                                card=int(input('Enter your payment card number: '))
                                print('Transaction Successful.')
                            print('The item(s) shall be delivered within 48 hours at',Ad,'.')
                            print('We shall keep you updated of the shipment of the goods on your contact number',P,'and email address',E,'.')
                            print('Thank you for shopping with us,',N,'. We hope to see you soon.')
                        elif _C=='N':
                            print('Dropped')
            elif B=='D004':
                print('Welcome to our book department.')
                print('Our products are listed below:')
                print()
                Q2='SELECT * FROM Books'
                c.execute(Q2)
                data2=list(c.fetchall())
                for x in data2:
                    print('Product No:',x[0])
                    print('Name:      ',x[1])
                    print('Author:    ',x[2])
                    print('Price:     ',x[3])
                    print()
                P = int(input('Select the product you wish to buy by entering its number: '))
                print()
                n=int(input('How many do you want?' ))
                print()
                print('The details of your chosen product are given below.')
                print()
                for x in data2:
                    if P==x[0]:
                        print('Product No:',x[0])
                        print('Name:      ',x[1])
                        print('Author:    ',x[2])
                        print('Price/Item:  ',x[3])
                        Price=x[3]
                        TotalPrice=Price*n
                        print('Total price: ',TotalPrice)            
                        print()
                        print('Do you confirm details of the product you wish to buy? (Y/N)')
                        _C=str(input()).upper()
                        if _C=='Y':
                            print('Please enter your following necessary details:')
                            N=str(input('Name: '))
                            P=int(input('Contact number: '))
                            E=str(input('Email address: '))
                            Ad=str(input('Address of delivery: '))
                            M=str(input('Would you like to pay through cash(C) or online(O)? ')).upper()
                            print("Amount to be paid:",TotalPrice)
                            if M=='C':
                                print('Please pay',TotalPrice,'to the deliverer of the goods.')
                            elif M=='O':
                                card=int(input('Enter your payment card number: '))
                                print('Transaction Successful.')
                            print('The item(s) shall be delivered within 48 hours at',Ad,'.')
                            print('We shall keep you updated of the shipment of the goods on your contact number',P,'and email address',E,'.')
                            print('Thank you for shopping with us,',N,'. We hope to see you soon.')
                        elif _C=='N':
                            print('Dropped')
            else:
                print('Code',B,'does not exist. Try again.')
                customer()
            X=str(input('Do you wish to continue shopping? (Y/N) ')).upper()
            chk=X
            if X=='N':
                print('Thank you for shopping at EShop. We hope to see you again soon.')
                break    
    customer()
#Staff Services
#Verification
elif U=='S':
    Psd=str(input('Enter the business passcode: '))
    ESP='R19028A'
    if Psd==ESP:
        i=str(input('Enter your staff ID: '))
        d=str(input('Enter your full name: '))
        c.execute("SELECT * FROM STAFF")
        sdata=list(c.fetchall())
        for x in sdata:
            if i==x[0]:
                if d==x[1]:
                    print('Welcome to EShop,',x[1],'.')
                    print("Let's get to work!")
                    print()
                    print("What would you like to do?")
                    print('1. View a table.')
                    print("2. View a table's structure.")
                    print("3. View a chart for sales in each department for year 2021.")
                    print()
                    S=int(input('Enter the service number: '))
                    #View tables
                    if S==1:
                          print('1. View the tables.')
                          print('Here are the tables in this database.')
                          print()
                          #Showing all tables
                          c.execute("SHOW TABLES")
                          Bdata1=c.fetchall()
                          n=len(Bdata1)
                          DL=[]
                          for x in Bdata1:
                              print(x[0])
                              DL.append(x[0])
                              print('-----------')
                          print()
                          N=input('Enter the name of the required table: ')
                          if N in DL:
                              #Showing the required table
                              c.execute("SELECT * FROM {}".format(N))
                              '''for table N,
                              colN has column names, Data has all records'''
                              colN=[i[0] for i in c.description]
                              nCol=len(c.description)
                              Data=c.fetchall()
                              print()                                  
                              for x in Data:
                                  Records=pd.Series(x,colN)
                                  print(Records)
                                  print()
                          else:
                              #Wrong table
                              print('Table',N,'is not in the database.')                                           
                    if S==2:
                        #Showing table structure
                        print("2. View a table's structure.")
                        print('Here are the tables in this database.')
                        print()
                        #Showing tablenames
                        c.execute("SHOW TABLES")
                        Bdata1=c.fetchall()
                        n=len(Bdata1)
                        DL=[]
                        for x in Bdata1:
                            print(x[0])
                            DL.append(x[0])
                            print('-----------')
                        print()
                        N=input('Enter the name of the required table: ')
                        if N in DL:
                            print('You have selected table',N)
                            print()
                            #Showing table structure
                            c.execute("DESC {}".format(N))
                            '''for desc table N,
                            colN has headings, Data has details'''
                            colN=[i[0] for i in c.description]
                            nCol=len(c.description)
                            Data=c.fetchall()
                            n=0
                            print()                            
                            for x in Data:
                                Desc=pd.Series(x,colN)
                                print(Desc)
                                print()
                        else:
                            #Wrong table
                            print('Table',N,'is not in the database.')
                    if S==3:
                        import matplotlib.pyplot as plt
                        Months=['January','February','March','April','May','June','July','August','September','October','November','December']
                        d=pd.read_csv("Sales2021.csv")
                        d.plot(kind='bar',x='Month',title='Sales in year 2021',color=list('rgby'))
                        plt.xlabel='Months'
                        plt.ylabel('Sales')
                        plt.show()
else:
    print('Incorrect choice entered.')
print()
print("THE END")
'''Complete'''
