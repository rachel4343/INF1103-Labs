# An Inventory is responsible for managing a collection of Products.

import json

from physical_product import PhysicalProduct
from digital_product import DigitalProduct


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

            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        # Display information for all products.
        if len(self.__products) == 0:
            print("\nInventory is empty.")
            return

        for product in self.__products:
            product.display_information()
            print()

    def load_inventory(self, filename):
        # Load the inventory from a JSON file.
        try:
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

            json.dump(
                [product.to_dict() for product in self.__products],
                file,
                indent=4
            )