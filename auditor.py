# Requirement 1
# Initialize the inventory to zero in the start
# git add auditor.py
# git commit -m "Initialize inventory"
# git status
# git log
inventory = 0

# Requirement 8
failed_entries = 0

# Requirement 2
# Run in a continuous loop asking user to enter a stock quantity, until the user 
# types quit. (Think of which loop might be helpful here: for or while) 
# git add auditor.py
# git commit -m "Add continuous stock input loop"
# git status
# git log
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
# git log
    if not stock.isdigit():
        print("Error: Invalid stock quantity.")
        failed_entries += 1
        continue

# Requirement 3
# Accept stock values as integers.
# git add auditor.py
# git commit -m "Add stock values as integers"
# git status
# git log
    stock = int(stock)

# Requirement 5
# Enforce business rules: Reject negative numbers.
# git add auditor.py
# git commit -m "Reject negative stock values"
# git status
# git log
    if stock < 0:
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue

# Requirement 6
# Manage State: Keep a running total of the inventory. 
# git add auditor.py
# git commit -m "Add running inventory total"
# git status
# git log
    inventory += stock
    print(f"Current inventory: {inventory}")

# Requirement 7
# Trigger Overstock Alert: If the total inventory exceeds 500 units, print an 
# alert and break the loop immediately.
# git add auditor.py
# git commit -m "Add inventory limit alert"
# git status
# git log
    if inventory > 500:
        print("Alert: Overstock! Inventory exceeds 500 units.")
        break

# Requirement 8
# Reporting: When the user types quit, print the Total Units Processed and the 
# Number of Failed/Rejected Entries.
# git add auditor.py
# git commit -m "Add final inventory report"
# git status
# git log
print("\n--- Inventory Report ---")
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")