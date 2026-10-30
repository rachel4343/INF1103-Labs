# Define a Product class with private attributes for product_id, name, price, and stock. 
# Product class should have one clear responsibility: Represent and manage a product. 
# The constructor initializes these attributes when a new Product object is created.

class Product:
    def __init__(self, product_id, name, price, stock):     # The constructor method initializes the Product object with the provided attributes.
        self.__product_id = product_id                      # The __ indicates that these attributes are intended to be private.
        self.__name = name                                  # Private attribute for the product name.
        self.__price = price                                # Private attribute for the product price.
        self.__stock = stock                                # Private attribute for the product stock.
    
    def get_product_id(self):                               # This public method returns the product ID of the product.
        return self.__product_id                            # Return the private product ID attribute.
    
    def update_stock(self, quantity):                       # This public method updates the stock quantity of the product.
        self.__stock = quantity                             # The stock attribute is updated to the new quantity provided by the parameter.

    def display_information(self):                          # This public method displays the product's information in a formatted manner.
        print(f"ID: {self.__product_id}")                   # Display the product ID.
        print(f"Name: {self.__name}")                       # Display the product name.
        print(f"Price: ${self.__price:.2f}")                # Display the product price formatted to 2 decimal places.
        print(f"Stock: {self.__stock}")                     # Display the product stock.

    def to_dict(self):                                      # This public method returns a dictionary representation of the product's attributes, which can be useful for saving or exporting product data.
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }