# Inventory Management System

# Requirement 1: Data Representation
# Store each product as a dictionary inside a list.

import json # allows Python to read and write JSON files.
import os # check whether a file exists.

# Requirement 3: Data Persistence
# Load inventory from inventory.json.
def load_inventory():
    # Check whether inventory.json exists.
    if not os.path.exists("inventory.json"):
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return []

    # Open the JSON file in read mode.
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    print("\ninventory.json found.")
    print("Inventory loaded successfully.")

    return inventory


# Save inventory to inventory.json.
def save_inventory(inventory):
    # Open the JSON file in write mode.
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


# Display all products in the inventory.
def display_all():
    print("\nCurrent Inventory")
    print("-" * 60)

    if not inventory:
        print("Inventory is empty.")
        return

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 60)


# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)

    # Load saved inventory.
    inventory = load_inventory()

    # Display the loaded inventory.
    display_all()