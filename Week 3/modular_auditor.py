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