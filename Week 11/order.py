# Order class represents a customer's order, which can contain multiple OrderLine objects. Each OrderLine represents a specific product and its quantity in the order. 
# The Order class provides methods to add and remove OrderLine objects, calculate the total cost of the order, and display the order details.
# Order class demonstrates composition, as it is composed of OrderLine objects, and the lifetime of the OrderLine objects is tied to the lifetime of the Order object. 
# When an Order is deleted, its associated OrderLine objects are also deleted.

from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy, NoDiscount

class Order:
    # Type hint: DiscountStrategy | None means accepts a strategy or None and = None means that the parameter is optional. If no strategy is provided, it defaults to None.
    def __init__(self, order_id: str, discount_strategy: DiscountStrategy | None = None):   # The constructor initializes the Order object with an order ID and an optional discount strategy. It takes two parameters: order_id (a string representing the unique identifier for the order) and discount_strategy (an instance of a class that implements the DiscountStrategy interface, or None if no discount strategy is provided).
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount_strategy: DiscountStrategy = discount_strategy or NoDiscount()
    
    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount_strategy = discount

    # This method adds a new OrderLine to the order by creating an OrderLine object with the specified product and quantity, and appending it to the order_lines list.
    # This demonstrates composition because the Order class is composed of OrderLine objects, and the lifetime of the OrderLine objects is tied to the lifetime of the Order object. When an Order is deleted, its associated OrderLine objects are also deleted.
    def add_order_line(self, product: Product, quantity: int) -> None:      # The method accepts a Product and quantity.
        order_line = OrderLine(product, quantity)                           # Order creates a new OrderLine.
        self.order_lines.append(order_line)                                 # Order stores the new OrderLine.

    # def remove_order_line(self, product_id: str) -> None:
    #     for order_line in self.order_lines:
    #         if order_line.product.get_product_id() == product_id:
    #             self.order_lines.remove(order_line)
    #             return

    def remove_order_line(self, index: int) -> None:                         # This method removes an OrderLine from the order_lines list based on the provided index. It checks if the index is valid (within the range of the list) before removing the OrderLine at that index.
        if 0 <= index < len(self.order_lines):                               # This checks if the index is valid (within the range of the list).
            self.order_lines.pop(index)                                      # Removes the OrderLine at the specified index from the order_lines list.

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)  # This method calculates the total cost of the order by summing the subtotals of all OrderLine objects in the order_lines list. It uses a generator expression to iterate through each OrderLine and call its calculate_subtotal() method, which returns the subtotal for that line item. The sum() function then adds up all the subtotals to get the total cost of the order.
        return self.discount_strategy.apply(total)                           # After calculating the total cost of the order, this line applies the discount strategy to the total. It calls the apply() method of the discount_strategy object, passing in the calculated total. The apply() method is defined in the DiscountStrategy interface and must be implemented by any concrete discount strategy class. 
                                                                             # This allows for different discount strategies to be applied to the order total, depending on the specific implementation of the discount strategy being used. The result is the final total cost of the order after applying any applicable discounts.                          

    def display_order(self) -> None:
        print(f"Order ID: {self.order_id}")
        print("-----------------------------")

        for order_line in self.order_lines:
            print(f"Product: {order_line.product.get_name()}")
            print(f"Quantity: {order_line.quantity}")
            print(f"Subtotal: ${order_line.calculate_subtotal():.2f}")
            print("-----------------------------")

        print(f"Total: ${self.calculate_total():.2f}")
