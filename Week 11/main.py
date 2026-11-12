
# Main program for the Lab 8 inventory management system.

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory
from inventory import Inventory
from order import Order


# --------------------------------------------------
# INPUT VALIDATION FUNCTIONS
# --------------------------------------------------

def get_non_empty_input(prompt: str) -> str:
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_int_input(prompt: str, minimum: int = 0) -> int:
    """Keep asking until the user enters a valid integer."""
    while True:
        try:
            value = int(input(prompt))

            if value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float_input(prompt: str, minimum: float = 0.0) -> float:
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            value = float(input(prompt))

            if value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_product_type() -> str:
    """Keep asking until the user selects a valid product type."""
    while True:
        print("\n1. Physical Product")
        print("2. Digital Product")

        product_type = input("Enter product type: ").strip()

        if product_type in ("1", "2"):
            return product_type

        print("Invalid product type. Please enter 1 or 2.")


# --------------------------------------------------
# CREATE INVENTORY
# --------------------------------------------------

inventory = Inventory()

# Store orders created during this program.
orders: list[Order] = []

# Load existing inventory.
inventory.load_inventory("inventory.json")


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

while True:

    print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Remove a product")
    print("6. Save inventory")
    print("7. Create an order")
    print("8. Display all orders")
    print("9. Exit")

    choice = input("Enter your choice: ").strip()

    # 1. Display all products
    if choice == "1":

        inventory.display_all_products()

    # 2. Add a product
    elif choice == "2":

        product_type = get_product_type()

        product_id = get_non_empty_input("Enter product ID: ")
        name = get_non_empty_input("Enter product name: ")
        price = get_float_input("Enter product price: ")
        stock = get_int_input("Enter product stock: ")

        # Create Supplier
        supplier_id = get_non_empty_input("Enter supplier ID: ")
        supplier_name = get_non_empty_input("Enter supplier name: ")
        supplier_email = get_non_empty_input("Enter supplier email: ")

        supplier = Supplier(
            supplier_id,
            supplier_name,
            supplier_email
        )

        # Create PhysicalProduct or DigitalProduct
        # Use the ProductFactory to create the appropriate product type based on user input. This approach adheres to the Factory design pattern, which encapsulates the object creation logic and allows for easy extension of new product types in the future without modifying existing code.
        # We have removed the responsibility of directly creating the product objects. Factory now handles that responsibility.
        if product_type == "1":

            weight = get_float_input("Enter product weight (kg): ")

            product = ProductFactory.create(
                "physical",
                product_id,
                name,
                price,
                stock,
                supplier,
                weight=weight
            )

        else:

            download_size = get_float_input("Enter download size (MB): ")

            product = ProductFactory.create(
                "digital",
                product_id,
                name,
                price,
                stock,
                supplier,
                download_size=download_size
            )

        inventory.add_product(product)

        print("Product added successfully.")

    # 3. Update stock
    elif choice == "3":

        product_id = get_non_empty_input(
            "Enter product ID to update stock: "
        )

        product = inventory.find_product(product_id)

        if product:

            quantity = get_int_input(
                "Enter new stock quantity: "
            )

            product.update_stock(quantity)

            print("Stock updated successfully.")

        else:
            print("Product not found.")

    # 4. Search for a product
    elif choice == "4":

        product_id = get_non_empty_input(
            "Enter product ID to search: "
        )

        product = inventory.find_product(product_id)

        if product:

            print("\nProduct found:")
            product.display_information()

        else:
            print("Product not found.")

    # 5. Remove a product
    elif choice == "5":

        product_id = get_non_empty_input(
            "Enter product ID to remove: "
        )

        product = inventory.find_product(product_id)

        if product:

            inventory.remove_product(product_id)

            print("Product removed from inventory.")

        else:
            print("Product not found.")

    # 6. Save inventory
    elif choice == "6":

        inventory.save_inventory("inventory.json")

        print("Inventory saved successfully.")

    # 7. Create an order
    elif choice == "7":

        order_id = get_non_empty_input("Enter order ID: ")

        order = Order(order_id)

        while True:

            product_id = input(
                "\nEnter product ID to add to order "
                "(or type 'done' to finish): "
            ).strip()

            if product_id.lower() == "done":
                break

            if not product_id:
                print("Product ID cannot be empty. Please try again.")
                continue

            product = inventory.find_product(product_id)

            if product:

                quantity = get_int_input(
                    "Enter quantity: ",
                    minimum=1
                )

                order.add_order_line(product, quantity)

                print("Product added to order.")

            else:
                print("Product not found in inventory.")

        if order.order_lines:

            orders.append(order)

            print("\nOrder created successfully.")

            order.display_order()

        else:
            print("\nNo products were added. Order was not created.")

    # 8. Display all orders
    elif choice == "8":

        if not orders:
            print("No orders have been created.")

        else:

            for order in orders:
                order.display_order()

    # 9. Exit
    elif choice == "9":

        print("Goodbye! Exiting the program...")
        break

    # Invalid menu choice
    else:

        print("Invalid choice. Please try again.")
