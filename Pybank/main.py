import os
import csv

#Joining the paths together 
csvpath = os.path.join('..','Resources', 'budget_data.csv')
print(csvpath)


#Opening the CSV file and breaking it out by commas for readability
with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

#assigning my variables
    months = 0 
    totalprofitloss = 0
    maxvalue = []
    minvalue = []
#starting the loop and printing out the rows   
    for row in csvreader:
        print(row)
#Add all of the months together          
        months += 1
#Adding together the total profit
        totalprofitloss = totalprofitloss + int(row[1])
#Finding the average profit       
        average = totalprofitloss/months
#Finding the Greatest Profit and Greatest Loss and the corresponding months     
        maxvalue.append(row[1])
        minvalue.append(row[1])

#Printing everything out         
print("Financial Analysis")
print("***********************")
print("Total number of months: " + str(months))
print("Total: $" + str(totalprofitloss))  
print("Average: $" +  str(average))
print("Greatest Profit: $" + (max(maxvalue) + row[0]))
print("Greatest Loss: $" + (min(minvalue) + row[0]))
