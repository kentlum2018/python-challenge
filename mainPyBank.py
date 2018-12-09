#for homework due 8Dec PyBank
# -*- coding: utf-8 -*-
# """
# Created on Mon Dec  3 17:11:56 2018
# finds the total of gains and losses and the diff between months

# @author: lumk4
# """

import csv
import os

#import the csv file and rename to budget_data
file_read = "C:/Users/lumk4/Desktop/class_work/hw2/PyBank_Resources_budget_data.csv"
row_cnt=0
Total = 0
amt=0
prev_amt=0
change = 0
greatest_chg=0
greatest_chg_date=""
greatest_loss=0
greatest_loss_date=""
avg = 0
f=open('PyBank_output.txt', 'w').close()
pathname = ("C:/Users/lumk4/Desktop/class_work/python-challenge/PyBank/PyBank_output.txt")

with open(file_read, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#read header
    csv_header = next(csvreader)
    
#generate grand total 
    for row in csvreader:
        row_cnt +=1
        amt= float(row[1])
        Total += amt
#to clear the header and find the changes between months        
        if row_cnt > 1:
            change += amt - prev_amt
#for the greatest pos change        
        if (amt-prev_amt) > greatest_chg:
            greatest_chg = amt-prev_amt
            greatest_chg_date = row[0]
#for the greatest neg change           
        if (amt-prev_amt) < greatest_loss:
            greatest_loss = amt-prev_amt
            greatest_loss_date = row[0]
#placeholder for the compare amt        
        prev_amt = amt


#display all output
print ('Financial Analysis')
print ('--------------------')
print ("Total Months :", row_cnt)
print ("Total: ", Total)
avg =(change/(row_cnt-1))
print ("Average : $", ("{0:.2f}".format(avg)))
print ("Greatest Increase in Profits: ",  greatest_chg_date, " ($", greatest_chg, ")")
print ("Greatest Loss in Profits: ", greatest_loss_date, " ($", greatest_loss, ")")

with open (pathname, 'w') as Bank_output:
    Bank_output.write('Financial Analysis')
    Bank_output.write("\n")
    Bank_output.write('--------------------')
    Bank_output.write("\n")
    Bank_output.write("Total Months :" +str(row_cnt))
    Bank_output.write("\n")

    Bank_output.write ("Total: " +str(Total))
    Bank_output.write("\n")
    avg =(change/(row_cnt-1))
    Bank_output.write ("Average : $" +str("{:.2f}".format(avg)))
    Bank_output.write("\n")
    Bank_output.write ("Greatest Increase in Profits: "+str(greatest_chg_date) )
    Bank_output.write (("($" +str(greatest_chg) ))
    Bank_output.write (")")
    Bank_output.write("\n")
    Bank_output.write ("Greatest Loss in Profits: " +str(greatest_loss_date))
    Bank_output.write (" ($" +str(greatest_loss))
    Bank_output.write(")")
#close file_read