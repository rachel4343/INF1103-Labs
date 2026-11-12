# OrderLine class represents a line item in an order, containing a product and its quantity.
# It has a method to calculate the subtotal for that line item based on the product's price and the quantity ordered.

from product import Product


class OrderLine:
    def __init__(self, product: Product, quantity: int):     # The constructor initializes the OrderLine object with a product and its quantity. It takes two parameters: product (an instance of the Product class) and quantity (an integer representing the number of units ordered).
        self.product: Product = product                      # The product attribute is an instance of the Product class, representing the product associated with this order line. This establishes a relationship between the OrderLine and Product classes.
        self.quantity: int = quantity                        # The quantity attribute is an integer representing the number of units of the product ordered in this order line. It is initialized with the value provided in the constructor.

    def calculate_subtotal(self) -> float:                   # This method calculates the subtotal for the order line by multiplying the product's price by the quantity ordered. It returns a float representing the subtotal amount.
        return self.product.get_price() * self.quantity      # Uses public getter: get_price() method of the Product class to retrieve the product's price and multiplies it by the quantity to calculate the subtotal. This follows encapsulation because OrderLine accesses Product's price through its public interface.
