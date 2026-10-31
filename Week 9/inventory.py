# An Inventory is responsible for managing a collection of Products.

import json

from physical_product import PhysicalProduct                           # The PhysicalProduct class is imported to allow the Inventory class to create instances of physical products when loading from a JSON file. 
from digital_product import DigitalProduct                             # The DigitalProduct class is imported to allow the Inventory class to create instances of digital products when loading from a JSON file.


class Inventory:

    def __init__(self):
        # Private attribute to store the list of Product objects.
        self.__products = []

    def add_product(self, product):
        # Add a Product object to the inventory.
        self.__products.append(product)

    def search_product(self, product_id):
        # Search for a Product in the inventory by its product ID.
        for product in self.__products:
            # Check if the product ID matches the search query.
            # Uses the get_product_id() method to access the product ID, adhering to encapsulation principles by not directly accessing private attributes of the Product class. This ensures that the Inventory class interacts with Product objects through their public interface, maintaining a clear separation of concerns and promoting code maintainability.
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        # Display information for all products.
        if len(self.__products) == 0:
            print("\nInventory is empty.")
            return

        for product in self.__products:
            # display_information() is a polymorphic method that behaves differently based on the type of Product (PhysicalProduct or DigitalProduct). This allows the Inventory class to call the same method on different product types without needing to know the specific details of each product type.
            product.display_information()
            print()

    def load_inventory(self, filename):
        # Load the inventory from a JSON file.
        try:
            # Open the specified JSON file in read mode and load its contents into a Python data structure using the json.load() function. This allows the Inventory class to deserialize the JSON data into Python objects, enabling it to reconstruct the inventory from a saved state.
            with open(filename, 'r') as file:
                data = json.load(file)

            for item in data:

                # Create the correct type of Product
                # based on the product type stored in JSON.
                if item["type"] == "physical":

                    product = PhysicalProduct(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["weight"]
                    )

                elif item["type"] == "digital":

                    product = DigitalProduct(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["download_size"]
                    )

                else:
                    print(
                        f"Unknown product type: {item['type']}"
                    )
                    continue

                self.add_product(product)

        except FileNotFoundError:
            print(
                "\nInventory file not found. "
                "Starting with an empty inventory."
            )

    def save_inventory(self, filename):
        # Save all Product objects to a JSON file.
        with open(filename, 'w') as file:
            # Use a list comprehension to convert each Product object to a dictionary representation using the to_dict() method. This ensures that the data is serialized in a format that can be easily saved to a JSON file, adhering to the principle of single responsibility by delegating the conversion of product attributes to the Product class itself.
            json.dump([product.to_dict() for product in self.__products], file, indent=4)