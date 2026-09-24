import os

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

# git add modular_auditor.py
# git commit -m "Add get_valid_input() function"
# git log


# Requirement 2
# process_delivery(current_total, new_value): Calculates the new total and returns it. 
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

# git add modular_auditor.py
# git commit -m "Add process_delivery() function"
# git status
# git log


# Requirement 3
# calculate_tax(amount): A new requirement! This function takes a delivery amount and returns the tax (10% of that specific delivery). 
def calculate_tax(amount):
    tax = amount * 0.10
    return tax

# git add modular_auditor.py
# git commit -m "Add calculate_tax() function"
# git status
# git log


# Requirement 4
# generate_report(total_units, failed_attempts): A dedicated function to print the final summary.
def generate_report(total_units, failed_attempts):
    print("\n--- Inventory Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

# git add modular_auditor.py
# git commit -m "Add generate_report() function"
# git status
# git log


# Requirement 5
# load_inventory(): Loads the saved inventory total and transaction history.
def load_inventory():
    if not os.path.exists("inventory.txt"):
        return 0, []

    with open("inventory.txt", "r") as file:
        lines = file.readlines()

    total = int(lines[0].strip())

    if len(lines) > 1 and lines[1].strip():
        history = [int(value) for value in lines[1].strip().split(",")]
    else:
        history = []

    return total, history


# Main program
# Initialize Requirements
inventory, history = load_inventory() # Initialize the inventory to call the function
deliveries_processed = 0 # Track the number of valid deliveries
failed_entries = 0 # Track the number of failed/rejected entries

while True:
    stock = get_valid_input()

    if stock == "quit":
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)

    tax = calculate_tax(stock)

    deliveries_processed += 1

    print(f"Current inventory: {inventory}")
    print(f"Tax for this delivery: {tax}")

    if inventory > 500:
        print("Alert: Overstock! Inventory exceeds 500 units.")
        break

generate_report(deliveries_processed, failed_entries)

# git add modular_auditor.py
# git commit -m "Add Complete modular auditor inventory"
# git status
# git log
# git push origin master