

### PyBank ###


import os
import csv

Pybankfile = "Resources\\budget_data.csv"

# Initialize variables to store data
months = 0
total_sum = 0
profit_losses = []  # To store the profit/losses values
dates = []  # To store dates

# open the file and read it
with open(Pybankfile, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    prev_profit_loss = 0  

    for row in csvreader:
        months =months + 1
        total_sum = total_sum + int(row[1])

        # Store the profit/loss value and date
        profit_loss = int(row[1])
        profit_losses.append(profit_loss)
        dates.append(row[0])

    print("Financial Analysis")
    print("**************************")
    print("Total Months: " + str(months))
    print("Total: $" + str(total_sum))

# Calculate changes in profit/losses
profit_loss_changes = [profit_losses[i] - profit_losses[i - 1] for i in range(1, len(profit_losses))]

# Calculate the average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and decrease
max_increase = max(profit_loss_changes)
max_decrease = min(profit_loss_changes)

# Find the corresponding dates for the greatest increase and decrease
max_increase_date = dates[profit_loss_changes.index(max_increase) + 1]
max_decrease_date = dates[profit_loss_changes.index(max_decrease) + 1]

# Print the results
print("Average Change: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + max_increase_date + " ($" + str(max_increase) + ")")
print("Greatest Decrease in Profits: " + max_decrease_date + " ($" + str(max_decrease) + ")")





# Export the results to a text file
with open("financial_analysis.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("**************************\n")
    txtfile.write("Total Months: " + str(months) + "\n")
    txtfile.write("Total: $" + str(total_sum) + "\n")
    txtfile.write("Average Change: $" + str(round(average_change, 2)) + "\n")
    txtfile.write("Greatest Increase in Profits: " + max_increase_date + " ($" + str(max_increase) + ")\n")
    txtfile.write("Greatest Decrease in Profits: " + max_decrease_date + " ($" + str(max_decrease) + ")\n")

print("Results have been exported to 'financial_analysis.txt'")

