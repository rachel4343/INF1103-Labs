# Initialize Requirements
inventory = 0 # Initialize the inventory to zero in the start
deliveries_processed = 0 # Track the number of valid deliveries
failed_entries = 0 # Track the number of failed/rejected entries

# Requirement 1
# get_valid_input(): Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal. 
def get_valid_input():
    stock = input("Enter stock quantity: ")

    if stock == "quit":
        return "quit"

    if not stock.isdigit():
        print("Error: Invalid stock quantity.")
        return None # tells the main program this entry was invalid.

    stock = int(stock)
    
    if stock < 0:
        print("Error: Stock quantity cannot be negative.")
        return None

    return stock


# # Requirement 6
# # Manage State: Keep a running total of the inventory. 
# # git add auditor.py
# # git commit -m "Add running inventory total"
# # git status
# # git log
#     inventory += stock
#     print(f"Current inventory: {inventory}")

# # Requirement 7
# # Trigger Overstock Alert: If the total inventory exceeds 500 units, print an 
# # alert and break the loop immediately.
# # git add auditor.py
# # git commit -m "Add inventory limit alert"
# # git status
# # git log
#     if inventory > 500:
#         print("Alert: Overstock! Inventory exceeds 500 units.")
#         break

# # Requirement 8
# # Reporting: When the user types quit, print the Total Units Processed and the 
# # Number of Failed/Rejected Entries.
# # git add auditor.py
# # git commit -m "Add final inventory report"
# # git status
# # git log
# print("\n--- Inventory Report ---")
# print(f"Total Units Processed: {inventory}")
# print(f"Number of Failed/Rejected Entries: {failed_entries}")