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

    