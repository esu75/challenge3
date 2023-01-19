# Author: Esubalew Adal
# This project is to create Python script to analyze the financial records of a company


#Importing required libraries
import os
import csv

# Getting the file path
budget_csv = os.path.join("PyBank\Resources", "budget_data.csv")
output_data = os.path.join('PyBank\Analysis', 'Report.txt') 

# List to collect all the values
Delta_Profit_Losses = []
dates = []

# Initialize counters or accumulators 

Total_Month = 0
Total = 0.0

with open(budget_csv) as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")
   
    Header = next(csv_reader)                           # Captures the header. 
    
    first_row = next(csv_reader )                       # captures on the row 1 values:['Jan-10', '1088983']
    
    Total_Month = Total_Month +1                        # This to capture row 1 value or month of Jan-10.Ohterwise, the final result will be # of rows-1
    Total = Total + int(first_row[1])                   # To capture row 1 value added. Otherwise, the final total will be less by row 1 value
    
    Prior_value = int(first_row[1])                     # This captures the first row [1] value for later calculation 
    
    #print(Delta)
    
    for i in csv_reader:
        
        # Calculate the total month
        
        Total_Month = Total_Month +1
        
        # Total profit/loss
        
        Total = Total + int(i[1])
        
        dates.append(i[0])
   
       
        # The harder part is next. Here the mathematical logic is: row[n+1] value - row[n] value to get the changes in profit/losses
        #To do this in python, I use a vatibale called 'Delta' to track the changes row-by-row
        #Then append all the 'Delta' values in a list variable called 'Delta_Profit_Losses'
        
        Delta = int(i[1]) - Prior_value   # This 'Prior_value' is just first row value from above
        
        # Append this value to Delta_Profit_Losses
        
        Delta_Profit_Losses.append(Delta)
        
        #we need to change the value for Prior_value from first row to all rows following rows i[1]
        
        Prior_value = int(i[1])  #This begins from second row to the end of the rows
        
        # Calculating the Delta average = sum of all the changes divided by the the total number
        
        Delta_Average = round(sum(Delta_Profit_Losses)/len(Delta_Profit_Losses),2)
        
        #greatest increase in profits (date and amount) over the entire period
        
        Greatest_Increase = max(Delta_Profit_Losses)
       
        Greatest_Increase_index = Delta_Profit_Losses.index(Greatest_Increase)
       
        Greatest_Increase_date = dates[Greatest_Increase_index] 
        
        #greatest decrease in profits (date and amount) over the entire period
        
        Greatest_Decrease = min(Delta_Profit_Losses)
        
        Greatest_Decrease_index = Delta_Profit_Losses.index(Greatest_Decrease)
        
        Greatest_Decrease_date = dates[Greatest_Decrease_index]
#Printing All The Results
    print("Financial Analysis")
    print("...................................")
    print(f"Total Months:{Total_Month}")
    print(f"Total:{Total}")
    print(f"Average Change:${Delta_Average}")
    print(f"Greatest Increase in Profits:{Greatest_Increase_date} (${Greatest_Increase})")
    print(f"Greatest Decrease in Profits:{Greatest_Decrease_date} (${ Greatest_Decrease})")

    # Exporting to text file

    Budget_data_Report = open(output_data, "w")
    Budget_data_Report.write(f"Financial Analysis\n" f"--------------------------------\n"
                             f"Total Months: {Total_Month}\n"f"Total: ${Total}\n"
                             f"Average Change: ${Delta_Average}\n" f"Greatest Increase in Profits: {Greatest_Increase_date} (${Greatest_Increase})\n"
                             f"Greatest Decrease in Profits: {Greatest_Decrease_date} (${Greatest_Decrease})\n" )




    
    