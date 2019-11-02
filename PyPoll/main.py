import os
import csv

#Joining the paths 
csvpath = os.path.join('..','Resources', 'copycsv.csv')
print(csvpath)

#Opening the CSV file and breaking it out by commas for readability
with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

#Assigning my variables
    totalvotes = 0
    candidate_options = []
    candidate_votes = {}

#Starting my loop
    for row in csvreader:
        print(row)
#Counting total number of votes        
        totalvotes += 1
#Printing out the names of the candidates and adding the number of votes that each candidate got      
        candidate_name = row[2]
         
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1 
#Finding the Winner based on votes              
        Winner = max(candidate_votes, key=candidate_votes.get)
        
        
#Printing out the results from the election
print("Election Results")
print("********************")
print("Total number of votes: " + str(totalvotes))
print("***************************")

#Printing out the percentages for each candidate
print("Khan: " + str((float(candidate_votes["Khan"])/float(totalvotes))*100), (int(candidate_votes["Khan"])))
print("Correy: " + str((float(candidate_votes["Correy"])/float(totalvotes))*100), (int(candidate_votes["Correy"])))
print("Li: " + str((float(candidate_votes["Li"])/float(totalvotes))*100), (int(candidate_votes["Li"])))
print("O'Tooley: " + str((float(candidate_votes["O'Tooley"])/float(totalvotes))*100),(int(candidate_votes["O'Tooley"])))
print("*******************************")
print("Winner: " + str(Winner))


