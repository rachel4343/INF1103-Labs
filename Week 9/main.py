# This is the main program that will run the inventory management system.

from physical_product import PhysicalProduct                      
from digital_product import DigitalProduct
from inventory import Inventory


inventory = Inventory()
inventory.load_inventory("inventory.json")


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
        # Ask the user what type of product they want to add.
        print("\n1. Physical Product")
        print("2. Digital Product")

        product_type = input("Enter product type: ")

        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        if product_type == "1":
            # Physical products need a weight.
            weight = float(input("Enter product weight (kg): "))

            product = PhysicalProduct(
                product_id,
                name,
                price,
                stock,
                weight
            )

        elif product_type == "2":
            # Digital products need a download size.
            download_size = float(
                input("Enter download size (MB): ")
            )

            product = DigitalProduct(
                product_id,
                name,
                price,
                stock,
                download_size
            )

        else:
            print("Invalid product type.")
            continue

        inventory.add_product(product)

        print("Product added successfully.")

    elif choice == "3":
        product_id = input("Enter product ID to update stock: ")

        product = inventory.search_product(product_id)

        if product:
            quantity = int(input("Enter new stock quantity: "))

            # Encapsulation:
            # The stock attribute is private, so we use the
            # public update_stock() method to modify it.
            product.update_stock(quantity)

            print("Stock updated successfully.")

        else:
            print("Product not found.")

    elif choice == "4":
        product_id = input("Enter product ID to search: ")

        # Encapsulation:
        # The product ID is private, so we use the public
        # search_product() method to find the product.
        product = inventory.search_product(product_id)

        if product:
            print("\nProduct found:")
            product.display_information()
            # get_fulfilment_info() shows abstract method implementation for fulfilment information, which is different for physical and digital products. This demonstrates polymorphism, where the same method name can have different implementations in different classes.
            print(f"Fulfilment: {product.get_fulfilment_info()}")

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