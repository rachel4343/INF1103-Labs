#  An Inventory is responsible for managing a collection of Products.

from product import Product


class Inventory:
    def __init__(self):                                   # The constructor method initializes the Inventory object with an empty list of products.
        self.__products = []                              # Private attribute to store the list of Product objects in the inventory.

    def add_product(self, product):                       # This public method adds a Product object to the inventory.
        self.__products.append(product)                   # Append the product to the private list.

    def search_product(self, product_id):                 # This public method searches for a Product in the inventory by its product ID.
        for product in self.__products:                   # Iterate through the list of products in the inventory.
            if product.get_product_id() == product_id:    # If the product ID matches, return the Product object.
                return product                            # Return the found Product object.

        return None

    def display_all(self):                                # This public method displays information for all products in the inventory.
        if len(self.__products) == 0:
            print("Inventory is empty.")
            return

        for product in self.__products:                   # Iterate through the list of products and call the display_information method for each product.
            product.display_information()
            print()