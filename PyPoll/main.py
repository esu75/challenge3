# Author: Esubalew Adal
# The purpose of the challenge is: 1. The total number of votes cast. 
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote


#Importing required libraries
import os
import csv

# Getting the file path
csv_path = os.path.join("PyPoll\Resources", "election_data.csv") # For reading the CSV file

output_data = os.path.join('PyPoll\Analysis', 'Report.txt')         # For writing on the analysis file (exporting file to txt)
Poll_data_Report = open(output_data, "w")  # Open for writing 

candidate_list = []  # list to hold the candidates names
Candidate_Vote = {}  # dictionary to hold the key (candidate names)and value

# initializing variables for later calculations 
Total_Votes = 0                     # The total votes collected 
Number_of_votes_won = 0              #The total number of votes each candidate won
percentage_of_votes_won = 0.0        # The percentage of votes each candidate won
Winner_percent = 0.0                 # Created for purpose of comparison reason to determine the winner
vote_count = 0                       # Created for purpose of comparison reason to determine the winner
winner_of_election_candidate = ""    #The winner of the election based on popular vote =  max(vote received/total vote)

# Command for printing on the terminal
print(f"Election Results\n" f"--------------------------------\n")

# Command for writing on the analysis file
Poll_data_Report.write(f"Election Results\n" f"--------------------------------\n")

#Opening the csv file for reading the content

with open(csv_path) as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
    Header = next(csvreader)    # Reads the header
    
    for i in csvreader:
        candidate_Name = i[2]
        County_Names   = i[1]

        Total_Votes = Total_Votes +1
    
       
    
    #comparing two lists
        
        if candidate_Name not in  candidate_list:

        # Adding candidate names to the list

            candidate_list.append(candidate_Name)
            
    
        # Assigning a  key (candidate_Names) and value to the dictionary 
            
            Candidate_Vote[candidate_Name] =0 

        Candidate_Vote[candidate_Name] = Candidate_Vote[candidate_Name] +1  # A dictionary: stores the names (keys) of the three candidates and their total vote each won (value)
   

    Total_Count = Total_Votes    # Added here for th epurpose of printing only 

    # Command for writing on the analysis file

    Poll_data_Report.write(f"Total Votes {Total_Count}\n"
    f"--------------------------------\n")

# Command for printing on the terminal
    print(f"Total Votes {Total_Count}")

# dictionary.get(keyname, value). Candidate_Vote is the dictionary. get() returns the VALUE of the item with the specified key.

    for candidate_Name in Candidate_Vote:

        Number_of_votes_won = Candidate_Vote.get(candidate_Name)   # Retreives the total number of votes each candidate won 

        percentage_of_votes_won = round(float(Number_of_votes_won)/float(Total_Votes )*100,3) #Retreieves the three candidates percent won

        Vote_data = (f"{candidate_Name}:{percentage_of_votes_won}% ({Number_of_votes_won}) ")

       # Command for printing on the terminal
        print(Vote_data)

        # Command for writing on the analysis file
        Poll_data_Report.write(f"{Vote_data}\n")
   
# Determining the winner of the election based on popular vote using 'if' condition 

        if (Number_of_votes_won > vote_count) and (percentage_of_votes_won > Winner_percent):
            vote_count = Number_of_votes_won
            winner_of_election_candidate = candidate_Name 
    
    final_Winner = (f"Winner:{winner_of_election_candidate}")

    # Command for printing on the terminal
    print(final_Winner)
    
    # Command for writing on the analysis file      
    Poll_data_Report.write(f"--------------------------------\n" f"Winner: {final_Winner}")
        
       
   
        

          