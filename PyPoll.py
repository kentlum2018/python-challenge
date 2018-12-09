# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:11:56 2018
finds the total of voters and winner of elec

@author: lumk4
"""
import csv
import os

#import the csv file and rename to budget_data
file_read = "C:/Users/lumk4/Desktop/class_work/python-challenge/PyPoll/election_data.csv"
row_cnt=0
Total = 0
#amt=0
#vote_tot=0
Khan_cnt = 0
Li_cnt = 0
Correy_cnt=0
OTooley_cnt=0
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
counts = [Khan_cnt , Correy_cnt, Li_cnt, OTooley_cnt]

winner = max(counts)

f=open('PyPoll_output.txt', 'w').close()
pathname = ("C:/Users/lumk4/Desktop/class_work/python-challenge/PyPollPyPoll_output.txt")



with open(file_read, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#read header
    csv_header = next(csvreader)
#create a dictionary of candidates and county
#candidates Khan Correy Li O'Tooley Other
#county Bamoo Marsh Queen Raffah Trandee Other
#calc the % that each candidate won
#determine the winner
#gen a output to the screen
#gen an export file of the results


#cnt the number of votes for each candidate
    for row in csvreader:
        row_cnt +=1
    
        if row[2] == candidate_list[0]:
           Khan_cnt +=1 
            
        if row[2] == candidate_list[1]:
           Correy_cnt +=1 
    
        if row[2] == candidate_list[2]:
           Li_cnt +=1 

        if row[2] == candidate_list[3]:
           OTooley_cnt +=1 

# counts = [Khan_cnt , Correy_cnt, Li_cnt, OTooley_cnt]
# win = max(counts)
Total += row_cnt
# print (win)
# Vote_tally = {"han": OTooley_cnt,"Khan": Khan_cnt , "Correy":Correy_cnt, "Li":Li_cnt}
# #Vote_tally = {"Khan": Khan_cnt , "Correy":Correy_cnt, "Li":Li_cnt, "O'Tooley":OTooley_cnt}
# print (Vote_tally)
# winner =  max (Vote_tally)
# print (winner)
# #winner = Vote_tally.values()
# print (counts[0])
# #print (candidate_list["Khan"][0])
#print (Khan_cnt)
# # print (type(counts))
# # winner = max (counts)
# print(winner)
# print (type (winner))
# print (Total)
# if OTooley_cnt > Khan_cnt and OTooley_cnt> Correy_cnt and OTooley_cnt>Li_cnt:
#     print ("Winner: O'Tooley")
# if Khan_cnt > OTooley_cnt  and Khan_cnt> Correy_cnt and Khan_cnt>Li_cnt:
#     print ("Winner: Khan")
# if  Correy_cnt> OTooley_cnt  and  Correy_cnt> Khan_cnt and Correy_cnt>Li_cnt:
#     print ("Winner: Correy")
# if  Li_cnt> OTooley_cnt  and  Li_cnt> Correy_cnt and Li_cnt > Khan_cnt:
#     print ("Winner: Li")



# #display all output
print ("Election Results")
print ('________________________')
print ("Total Votes: ", Total)
print ('________________________')
print ("Khan: ", "{0:.2f}".format(Khan_cnt/Total*100), "%","(" , Khan_cnt, ")")
print ("Correy: ", "{0:.2f}".format(Correy_cnt/Total*100), "%","(" , Correy_cnt, ")")
print ("Li: ", "{0:.2f}".format(Li_cnt/Total*100), "%","(" , Li_cnt, ")")
print ("O'Tooley: ", "{0:.2f}".format(OTooley_cnt/Total*100), "%","(" , OTooley_cnt, ")")
print ('________________________')
if OTooley_cnt > Khan_cnt and OTooley_cnt> Correy_cnt and OTooley_cnt>Li_cnt:
    print ("Winner: O'Tooley")
if Khan_cnt > OTooley_cnt  and Khan_cnt> Correy_cnt and Khan_cnt>Li_cnt:
    print ("Winner: Khan")
if  Correy_cnt> OTooley_cnt  and  Correy_cnt> Khan_cnt and Correy_cnt>Li_cnt:
    print ("Winner: Correy")
if  Li_cnt> OTooley_cnt  and  Li_cnt> Correy_cnt and Li_cnt > Khan_cnt:
    print ("Winner: Li")

if (Total) != (OTooley_cnt + Li_cnt + Correy_cnt + Khan_cnt):
    print ("FRAUD")

#write to file
with open (pathname, 'w') as Poll_output:
    Poll_output.write("Election Results")
    Poll_output.write("\n")
    Poll_output.write('--------------------')
    Poll_output.write("\n")
    Poll_output.write(("Total Votes: "+str(Total)))
    Poll_output.write("\n")
    Poll_output.write('--------------------')
    Poll_output.write("\n")
    Poll_output.write(("Khan: " +str("{0:.2f}".format(Khan_cnt/Total*100))))
    Poll_output.write( "% (" +str(Khan_cnt))
    Poll_output.write( ")")
    Poll_output.write("\n")
    Poll_output.write (("Correy: " +str("{0:.2f}".format(Correy_cnt/Total*100))))
    Poll_output.write( "% (" +str(Correy_cnt))
    Poll_output.write( ")")
    Poll_output.write("\n")
    Poll_output.write (("Li: " +str("{0:.2f}".format(Li_cnt/Total*100))))
    Poll_output.write("% (" +str(Li_cnt))
    Poll_output.write( ")")
    Poll_output.write("\n")
    Poll_output.write (("O'Tooley: " +str("{0:.2f}".format(OTooley_cnt/Total*100))))
    Poll_output.write("% (" +str(OTooley_cnt))
    Poll_output.write( ")")
    Poll_output.write("\n")
    Poll_output.write('--------------------')
    Poll_output.write("\n")
    if OTooley_cnt > Khan_cnt and OTooley_cnt> Correy_cnt and OTooley_cnt>Li_cnt:
       Poll_output.write ("Winner: O'Tooley")
    if Khan_cnt > OTooley_cnt  and Khan_cnt > Correy_cnt and Khan_cnt > Li_cnt:
       Poll_output.write ("Winner: Khan")
    if  Correy_cnt> OTooley_cnt and  Correy_cnt> Khan_cnt and Correy_cnt>Li_cnt:
       Poll_output.write ("Winner: Correy")
    if  Li_cnt> OTooley_cnt and Li_cnt> Correy_cnt and Li_cnt > Khan_cnt:
       Poll_output.write ("Winner: Li")




