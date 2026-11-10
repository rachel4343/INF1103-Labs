# This is the PhysicalProduct class that inherits from the Product class. 
# It adds an additional attribute for weight and overrides the display_information method to include weight information.
from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped                            # The PhysicalProduct class inherits from the CanBeShipped interface, allowing it to provide an implementation for the calculate_shipping_cost method. This enables polymorphism, where different classes can provide their own implementation of the shipping cost calculation while adhering to the same interface.


class PhysicalProduct(Product, CanBeShipped):                      # The PhysicalProduct class inherits from the Product class, allowing it to utilize the attributes and methods of the Product class while adding its own unique attribute for weight. And it also inherits from the CanBeShipped interface, allowing it to provide an implementation for the calculate_shipping_cost method.
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier):  # The supplier parameter is an instance of the Supplier class, representing the supplier associated with the product. This establishes a relationship between the Product and Supplier classes, allowing for better organization and management of product and supplier information.
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight
    
    def display_information(self) -> None:                         # This method overrides the display_information method from the Product class to include weight information. It first calls the parent class's display_information method to display the common product attributes, and then it adds the weight information specific to physical products. This demonstrates polymorphism, where the same method name can have different implementations in different classes.
        # Run the parent's display_information() first.
        super().display_information()                              # The super() function is used to call the display_information method of the parent Product class, ensuring that the common product attributes are displayed before adding the weight information. This maintains a clear separation of concerns and adheres to the principle of single responsibility by allowing each class to manage its own specific attributes and behaviors.
        # Adds the PhysicalProduct-specific information
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:                           # This method provides fulfilment information specific to physical products. It returns a string indicating that the product requires physical shipping. This method is an implementation of the abstract method defined in the Product class, fulfilling the contract established by the abstract base class and ensuring that subclasses provide specific functionality related to fulfilment information.
        return "This product requires physical shipping."          # Return a string indicating that the product requires physical shipping, providing fulfilment information specific to physical products.

    def calculate_shipping_cost(self) -> float:                     # This method provides an implementation for the calculate_shipping_cost method defined in the CanBeShipped interface. It calculates the shipping cost based on the weight of the physical product, returning a cost value.
        return self.__weight * 2                                   # Return the calculated shipping cost based on the weight of the physical product, providing a specific implementation for the shipping cost calculation as required by the CanBeShipped interface.

    def to_dict(self) -> dict:                                      # This public method returns a dictionary representation of the physical product's attributes, which can be useful for saving or exporting product data. It extends the to_dict method from the Product class to include the product type and weight information specific to physical products.
        data = super().to_dict()                                   # The super() function is used to call the to_dict method of the parent Product class, ensuring that the common product attributes are included in the dictionary representation before adding the product type and weight information specific to physical products. 
        data["type"] = "physical"                                  # Add the product type information to the dictionary, indicating that this is a physical product.
        data["weight"] = self.__weight                             # Add the weight information to the dictionary, providing a complete representation of the physical product's attributes for saving or exporting purposes.
        return data