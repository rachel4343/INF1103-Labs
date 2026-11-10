# An Inventory is responsible for managing a collection of Products.

import json
from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct                           # The PhysicalProduct class is imported to allow the Inventory class to create instances of physical products when loading from a JSON file. 
from digital_product import DigitalProduct                             # The DigitalProduct class is imported to allow the Inventory class to create instances of digital products when loading from a JSON file.


class Inventory:

    def __init__(self):
        # Private attribute to store the list of Product objects.
        self.products: list[Product] = []

    # The -> None is a return type hint.
    def add_product(self, product: Product) -> None: # This method receives a Product object and adds it to the Inventory's collection of products. It appends the Product to the list of products, allowing the Inventory to manage and keep track of the products it contains.
        self.products.append(product)

    def remove_product(self, product_id: str) -> None: # We receive a Product ID rather than a Product object. We search for the matching Product and remove its reference from the list.
        for product in self.products:
            if product.get_product_id() == product_id:
                self.products.remove(product)          # This removes the Product from the Inventory collection, not necessarily from memory.
                return
            
    def find_product(self, product_id: str) -> Product | None: # We receive a Product ID and search for the matching Product in the Inventory. If found, we return the Product object; otherwise, we return None. This is an optional return type.
        for product in self.products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all_products(self) -> None: # This method iterates through all Product objects in the Inventory and calls their display_information() method to print their details. It provides a way to view the information of all products managed by the Inventory.
        if not self.products:
            print("No products in inventory.")
            return
        
        for product in self.products:       # LSP: They should accept and manage Product objects rather than checking for specific subclasses unnecessarily.
            product.display_information()
            print(f"Fulfilment: {product.get_fulfilment_info()}")
            print("-----------------------------")

    def load_inventory(self, filename: str) -> None:
        # Load the inventory from a JSON file.
        try:
            # Open the specified JSON file in read mode and load its contents into a Python data structure using the json.load() function. This allows the Inventory class to deserialize the JSON data into Python objects, enabling it to reconstruct the inventory from a saved state.
            with open(filename, 'r') as file:
                data = json.load(file)

            for item in data:

                # Reconstruct the Supplier object
                supplier_data = item.get("supplier", {
                    "supplier_id": "S000",
                    "name": "Unknown Supplier",
                    "contact_email": "unknown@example.com"
                })

                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )

                # Reconstruct the correct Product subclass
                if item["type"] == "physical":

                    product = PhysicalProduct(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["weight"],
                        supplier
                    )

                elif item["type"] == "digital":

                    product = DigitalProduct(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["download_size"],
                        supplier
                    )

                else:
                    print(f"Unknown product type: {item['type']}")
                    continue

                self.add_product(product)

        except FileNotFoundError:
            print("\nInventory file not found. Starting with an empty inventory.")

    def save_inventory(self, filename: str) -> None:
        # Save all Product objects to a JSON file.
        with open(filename, 'w') as file:
            # Use a list comprehension to convert each Product object to a dictionary representation using the to_dict() method. This ensures that the data is serialized in a format that can be easily saved to a JSON file, adhering to the principle of single responsibility by delegating the conversion of product attributes to the Product class itself.
            json.dump([product.to_dict() for product in self.products], file, indent=4)