import os

# Requirement 1
# get_valid_input(): Gets the product name and quantity from the user.
def get_valid_input():

    # Ask the user to enter a product name.
    product_name = input("Enter Product Name ('quit' to end): ")

    # Allow the user to quit before entering a quantity.
    if product_name.lower() == "quit":
        return "quit"

    # Keep asking for the quantity until a valid one is entered.
    while True:

        # Ask the user to enter the quantity.
        quantity = input("Enter Quantity: ").strip()

        # Check whether the quantity contains only digits.
        if not quantity.isdigit():
            print("Error: Invalid quantity.")
            continue # Skips the current iteration and starts the next iteration of the loop it belongs to.

        # Convert the quantity from text into an integer.
        quantity = int(quantity)

        # Check that the quantity is greater than 0.
        if quantity <= 0:
            print("Error: Quantity must be greater than 0.")
            continue

        # Return both the product name and quantity.
        return product_name, quantity


# Requirement 2
# load_inventory(): Loads the saved orders from inventory.txt.
def load_inventory():

    # Check whether inventory.txt exists.
    if not os.path.exists("inventory.txt"):

        # If the file does not exist,
        # start with an empty order list.
        return []

    # Open inventory.txt in read mode.
    with open("inventory.txt", "r") as file:

        # Read all lines from the file.
        lines = file.readlines()

    # Create an empty list to store the order history.
    history = []

    # Read every line in the file.
    for line in lines:

        # Remove the newline character and extra spaces.
        line = line.strip()

        # Only add non-empty lines to the history.
        if line:
            history.append(line)

    # Return the complete order history.
    return history


# Requirement 3
# save_inventory(): Saves the order history to inventory.txt.
def save_inventory(history):

    # Open inventory.txt in write mode.
    # If the file does not exist, Python creates it.
    # If it already exists, the old contents are replaced.
    with open("inventory.txt", "w") as file:

        # Write every order from the history list.
        for order in history:

            # Write the order and move to the next line.
            file.write(order + "\n")


# # Requirement 3
# # load_inventory(): Loads the saved inventory total and transaction history.
# def load_inventory():
#     if not os.path.exists("inventory.txt"): # If inventory.txt DOES NOT exist in the current folder...
#         return 0, [] # Start the inventory at 0, Start with an empty transaction history.

#     with open("inventory.txt", "r") as file: # Open inventory.txt in "r" read mode.
#         lines = file.readlines() # This takes everything inside inventory.txt and puts it into a Python list.
#         # Example inventory.txt:
#         # 350
#         # 100,200,50
#         # becomes approximately:
#         # lines = ["350\n", "100,200,50"]

#     total = int(lines[0].strip()) # Take the first line of the file and convert text into an integer and store in variable "total".

#     if len(lines) > 1 and lines[1].strip(): # If there is a second line AND that second line contains something...
#         history = [int(value) for value in lines[1].strip().split(",")] # This line splits the second line of the file by commas and converts each value from a string into an integer, storing all the transaction amounts in the history list.
#     else:
#         history = [] # If the file doesn't have a second line, or the second line is empty: return empty history

#     return total, history # Return BOTH pieces of information to the main program:
#                           # total = the saved inventory total
#                           # history = the saved list of transaction amounts


# Requirement 4
# generate_report(): Displays the final contents of inventory.txt.
def generate_report(history):

    # Display the report heading.
    print("\n--- Final Inventory Report ---")

    # Display the total number of orders.
    print(f"\nTotal Orders: {len(history)}")

    # Check whether there are any orders.
    if not history:
        print("No orders found.")
        return

    # Display every order in the inventory.
    for order in history:
        print(order)


# Main program
# Load the previously saved order history.
history = load_inventory()



# # Requirement Testing
# # Create a list to store every valid transaction amount entered.
# transaction_history = []



# Display the existing orders.
print("\nCurrent Orders:")

# Display every order stored in the history list.
for order in history:
    print(order)

# Continue asking the user for new orders.
while True:

    # Get the product name and quantity.
    result = get_valid_input()

    # If the user types "quit", stop the program.
    if result == "quit":
        save_inventory(history)
        break

    # If the input is invalid, ask again.
    if result is None: # Exits the entire function and sends None back to the main program.
        continue

    # Separate the product name and quantity.
    product_name, quantity = result

    # Generate the next order ID.
    # 1001 is the first order ID.
    order_id = 1001 + len(history)

    # Create the new order as a string.
    new_order = f"{order_id}, {product_name}, {quantity}"

    # Add the new order to the history list.
    history.append(new_order)



    # # Requirement Testing
    # # Store the valid transaction amount in the history list.
    # transaction_history.append(quantity)

    # # Display the transaction history for testing.
    # print(f"Transaction History: {transaction_history}")



    # Display the newly added order.
    print("\nNew Order Added:")
    print(new_order)

    # Save the updated order history to inventory.txt.
    save_inventory(history)

    # Tell the user that the order was saved.
    print("\nOrder successfully saved to inventory.txt")


# Display the final inventory report.
generate_report(history)

# git add modular_auditor.py
# git commit -m "Add Complete modular auditor inventory"
# git status
# git log
# git push origin master