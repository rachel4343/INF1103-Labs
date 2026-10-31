# This is the PhysicalProduct class that inherits from the Product class. 
# It adds an additional attribute for weight and overrides the display_information method to include weight information.
from product import Product


class PhysicalProduct(Product):                                    # The PhysicalProduct class inherits from the Product class, allowing it to utilize the attributes and methods of the Product class while adding its own unique attribute for weight.
    def __init__(self, product_id, name, price, stock, weight):    # The constructor method initializes the PhysicalProduct object with the provided attributes, including weight.
        super().__init__(product_id, name, price, stock)           # The super() function is used to call the constructor of the parent Product class, ensuring that the product_id, name, price, and stock attributes are initialized properly. It follows the principle of single responsibility by delegating the initialization of common product attributes to the Product class.
        self.__weight = weight                                     # The __weight attribute is a private attribute that stores the weight of the physical product, encapsulating this information within the PhysicalProduct class.

    def display_information(self):                                 # This method overrides the display_information method from the Product class to include weight information. It first calls the parent class's display_information method to display the common product attributes, and then it adds the weight information specific to physical products. This demonstrates polymorphism, where the same method name can have different implementations in different classes.
        # Run the parent's display_information() first.
        super().display_information()                              # The super() function is used to call the display_information method of the parent Product class, ensuring that the common product attributes are displayed before adding the weight information. This maintains a clear separation of concerns and adheres to the principle of single responsibility by allowing each class to manage its own specific attributes and behaviors.
        # Adds the PhysicalProduct-specific information
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):                                 # This method provides fulfilment information specific to physical products. It returns a string indicating that the product requires physical shipping. This method is an implementation of the abstract method defined in the Product class, fulfilling the contract established by the abstract base class and ensuring that subclasses provide specific functionality related to fulfilment information.
        return "This product requires physical shipping."          # Return a string indicating that the product requires physical shipping, providing fulfilment information specific to physical products.