# Requirement 1
# Initialize the inventory to zero in the start
# git add auditor.py
# git commit -m "Initialize inventory"
# git status
inventory = 0

# Requirement 2
# Run in a continuous loop asking user to enter a stock quantity, until the user 
# types quit. (Think of which loop might be helpful here: for or while) 
# git add auditor.py
# git commit -m "Add continuous stock input loop"
# git status
while True:
    stock = input("Enter stock quantity: ")
    if stock == "quit":
        break

# Requirement 4
# Handle invalid input: If the user enters a string (e.g., "ten"), reject it, print an 
# error, and move to the next iteration. (Hint: use.isdigit()).
# git add auditor.py
# git commit -m "Reject invalid stock input"
# git status
    if not stock.isdigit():
        print("Error: Invalid stock quantity.")
        continue

# Requirement 3
# Accept stock values as integers.
# git add auditor.py
# git commit -m "Add stock values as integers"
# git status
    stock = int(stock)