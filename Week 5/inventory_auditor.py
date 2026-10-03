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


# Search for a product using its ID.
def search_product():
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip().upper()

    # Search through the inventory list.
    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found")
            print("-" * 40)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("-" * 40)
            return

    # Display this message if no matching product exists.
    print("Product not found.")


# Add a new product to the inventory.
def add_product():
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip().upper()

    # Check whether the product ID already exists.
    for product in inventory:
        if product["id"] == product_id:
            print("Error: Product ID already exists.")
            return

    # Ask for the product name.
    name = input("Product Name: ").strip()

    if not name:
        print("Error: Product name cannot be empty.")
        return

    # Validate the product price.
    try:
        price = float(input("Price: "))

        if price < 0:
            print("Error: Price cannot be negative.")
            return

    except ValueError:
        print("Error: Please enter a valid price.")
        return

    # Validate the stock quantity.
    try:
        stock = int(input("Stock Quantity: "))

        if stock < 0:
            print("Error: Stock cannot be negative.")
            return

    except ValueError:
        print("Error: Please enter a whole number for stock.")
        return

    # Create a dictionary for the new product.
    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    # Add the dictionary to the inventory list.
    inventory.append(new_product)

    print("\nProduct added successfully!")


# Update the stock quantity of an existing product.
def update_stock():
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip().upper()

    # Find the product using its ID.
    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            # Ask for the new stock quantity.
            try:
                new_stock = int(input("\nNew Stock Quantity: "))

                if new_stock < 0:
                    print("Error: Stock cannot be negative.")
                    return

            except ValueError:
                print("Error: Please enter a whole number.")
                return

            # Update the dictionary.
            product["stock"] = new_stock

            print("\nStock updated successfully!")
            return

    print("Product not found.")


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

    # Keep showing the menu until the user exits.
    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("\nEnter option: ").strip()

        if option == "1":
            display_all()

        elif option == "2":
            add_product()

        elif option == "3":
            update_stock()

        elif option == "4":
            search_product()

        elif option == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)

        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")