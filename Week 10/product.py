# Define a Product class with private attributes for product_id, name, price, and stock. 
# Product class should have one clear responsibility: Represent and manage a product. 
# The constructor initializes these attributes when a new Product object is created.

from abc import ABC, abstractmethod                         # The Product class inherits from the ABC (Abstract Base Class) module, allowing it to define abstract methods that must be implemented by any subclass. This enforces a contract for subclasses to provide specific functionality, ensuring consistency and adherence to the principles of object-oriented programming.
from supplier import Supplier

class Product(ABC):
    @abstractmethod                                         # The @abstractmethod decorator is used to define an abstract method, which means that any subclass of Product must implement this method. Every child class MUST provide its own version of this method. This enforces a contract for subclasses to provide specific functionality related to fulfilment information.
    def get_fulfilment_info(self):                          # The get_fulfilment_info method is defined as an abstract method, meaning that any subclass of Product must implement this method. This enforces a contract for subclasses to provide specific functionality related to fulfilment information, ensuring consistency and adherence to the principles of object-oriented programming.
        pass                                                # The pass statement is used as a placeholder for the abstract method, indicating that it does not have an implementation in the Product class. Subclasses must provide their own implementation of this method to fulfill the contract defined by the abstract base class.

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):  # The supplier parameter is an instance of the Supplier class, representing the supplier associated with the product. This establishes a relationship between the Product and Supplier classes, allowing for better organization and management of product and supplier information.
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier                  # The supplier attribute is an instance of the Supplier class, representing the supplier associated with the product. This establishes a relationship between the Product and Supplier classes, allowing for better organization and management of product and supplier information.
                                                            # This stores an actual Supplier object. This means we can do product.supplier.display_information() and it will call the display_information method of the Supplier class, allowing us to access and display the supplier's information directly from the product object. This is the association relationship.
    
    def get_product_id(self) -> str:                        # This public method returns the product ID of the product.
        return self.__product_id                            # Return the private product ID attribute.

    def get_name(self) -> str:                              # This public method returns the name of the product.
        return self.__name                                  # Return the private name attribute.

    def get_price(self) -> float:                           # This public method returns the price of the product.
        return self.__price                                 # Return the private price attribute.

    def update_stock(self, quantity: int) -> None:          # This public method updates the stock quantity of the product.
        self.__stock = quantity                             # The stock attribute is updated to the new quantity provided by the parameter.

    def display_information(self) -> None:                  # This public method displays the product's information in a formatted manner.
        print(f"ID: {self.__product_id}")                   # Display the product ID.
        print(f"Name: {self.__name}")                       # Display the product name.
        print(f"Price: ${self.__price:.2f}")                # Display the product price formatted to 2 decimal places.
        print(f"Stock: {self.__stock}")                     # Display the product stock.
        
    def to_dict(self) -> dict:                                      # This public method returns a dictionary representation of the product's attributes, which can be useful for saving or exporting product data.
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.supplier.to_dict()             # This calls the to_dict method of the Supplier class to get a dictionary representation of the supplier's attributes. This allows for easy serialization of the product and its associated supplier information into a format that can be saved or exported, such as JSON.
        }


# product = Product("P001", "Test", 10, 5)
# TypeError: Can't instantiate abstract class Product without an implementation for abstract method 'get_fulfilment_info'
# This is because the Product class is an abstract class and cannot be instantiated directly. It serves as a blueprint for other classes (like PhysicalProduct and DigitalProduct) that inherit from it and implement the abstract method get_fulfilment_info.