
#### PYPOLL ####

import os
import csv


PYPOLLfile = "Resources\\election_data.csv"




# Initialize variables and data structures
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(PYPOLLfile, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)
    
    for row in csvreader:
        # Count total votes
        total_votes = total_votes + 1
        
        # Get the candidate name from the row
        candidate = row[2]
        
        # If the candidate is not in the candidates dictionary, add them
        if candidate not in candidates:
            candidates[candidate] = 0
        
        # Increment the candidate's vote count
        candidates[candidate]= candidates[candidate] + 1

# Print the total number of votes cast
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Initialize a variable to keep track of the winner's vote count
winner_votes = 0

# Loop through candidates and calculate and print their statistics
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check if this candidate has the most votes so far
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

print("-------------------------")
# Print the winner
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print("Results have been exported to 'election_results.txt'")