# This is the main program that will run the inventory management system. It imports the Product and Inventory classes from their respective modules. 
# The program creates an instance of the Inventory class and then displays a menu to the user, allowing them to interact with the inventory system. 

# displaying the menu
# getting user input
# calling Inventory methods


from product import Product                                          # Import the Product class from the product module.
from inventory import Inventory                                      # Import the Inventory class from the inventory module.


inventory = Inventory()                                              # Create an instance of the Inventory class to manage the collection of products.

while True:
    print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Save inventory")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.display_all()

    elif choice == "2":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        product = Product(product_id, name, price, stock)

        inventory.add_product(product)

        print("Product added successfully.")

    elif choice == "3":
        product_id = input("Enter product ID to update stock: ")

        product = inventory.search_product(product_id)

        if product:
            quantity = int(input("Enter new stock quantity: "))
            product.update_stock(quantity)                           # Encapsulation. The stock attribute is private, so we use the public method update_stock to modify it.
            print("Stock updated successfully.")
        else:
            print("Product not found.")

    elif choice == "4":
        product_id = input("Enter product ID to search: ")

        product = inventory.search_product(product_id)               # Encapsulation. The product_id attribute is private, so we use the public method search_product to find the product in the inventory.

        if product:
            print("\nProduct found:")
            product.display_information()                            # Encapsulation. The attributes of the Product class are private, so we use the public method display_information to access and display them.
        else:
            print("Product not found.")

    elif choice == "5":
        inventory.save_inventory("inventory.json")
        print("Inventory saved successfully.")

    elif choice == "6":
        print("Goodbye! Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")