# This is the DigitalProduct class that inherits from the Product class.
# It adds an additional attribute for download_size and overrides the display_information method to include download size information.
from product import Product


class DigitalProduct(Product):                                          # The DigitalProduct class inherits from the Product class, allowing it to utilize the attributes and methods of the Product class while adding its own unique attribute for download size.
    def __init__(self, product_id, name, price, stock, download_size):  # The constructor method initializes the DigitalProduct object with the provided attributes, including download size.
        super().__init__(product_id, name, price, stock)                # The super() function is used to call the constructor of the parent Product class, ensuring that the product_id, name, price, and stock attributes are initialized properly. It follows the principle of single responsibility by delegating the initialization of common product attributes to the Product class.
        self.__download_size = download_size                            # The __download_size attribute is a private attribute that stores the download size of the digital product, encapsulating this information within the DigitalProduct class.

    def display_information(self):                                      # This method overrides the display_information method from the Product class to include download size information. It first calls the parent class's display_information method to display the common product attributes, and then it adds the download size information specific to digital products. This demonstrates polymorphism, where the same method name can have different implementations in different classes.
        # Run the parent's display_information() first.
        super().display_information()                                   # The super() function is used to call the display_information method of the parent Product class, ensuring that the common product attributes are displayed before adding the download size information. This maintains a clear separation of concerns and adheres to the principle of single responsibility by allowing each class to manage its own specific attributes and behaviors.
        # Adds the DigitalProduct-specific information
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self):                                      # This method provides fulfilment information specific to digital products. It returns a string indicating that the product is delivered digitally. This method is an implementation of the abstract method defined in the Product class, fulfilling the contract established by the abstract base class and ensuring that subclasses provide specific functionality related to fulfilment information.
        return "This product is delivered digitally."                   # Return a string indicating that the product is delivered digitally, providing fulfilment information specific to digital products.