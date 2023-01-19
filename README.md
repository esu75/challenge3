# challenge3
challenge 3 has two files:
1. PyBank
2. PyPoll
Each file has 3 separate files embedded in it:
1. The csv file
2. The Analysis text file (report)
3. The python code
4.The python code runs perfectly on the python terminal, however, may not run on the Bash terminal. If anyone is interested to run the code on the Bash termina, the path of the scv file location should be changed as follows:- For example for the PyBank: The path for the python code is "os.path.join("PyBank\Resources", "budget_data.csv")" extension and this runs only on python terminal. To run same code on Bash terminal, remove the "PyBank\" and change it to ("Resources", "budget_data.csv"). Do same thing for PyPoll. But, I beleive the python terminal is good for this challenge.

In this challenge, the PyBank code was not that difficult, however, the PyPoll analysis text file was challenging for me: The PyPoll code txt file has to print three candidate names and their vote counts. The total vote has to print once. The winner name has to print once.
Now, when exporting the txt, I created the output data path but in order to write to it at the end of the code like I did for the PyBank was not working due to the fact that the code just keep printing only one candidate name. The problem was on line # 78 for loop. The terminal has to print three names before exiting the loop.
To resolve the issue, I used a technique of printing the three items separately after each loop.

In general, I beleive I did learn a lot from these challenges!

Thank you,
Adal
