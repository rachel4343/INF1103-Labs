# Order class represents a customer's order, which can contain multiple OrderLine objects. Each OrderLine represents a specific product and its quantity in the order. 
# The Order class provides methods to add and remove OrderLine objects, calculate the total cost of the order, and display the order details.
# Order class demonstrates composition, as it is composed of OrderLine objects, and the lifetime of the OrderLine objects is tied to the lifetime of the Order object. 
# When an Order is deleted, its associated OrderLine objects are also deleted.

from product import Product
from order_line import OrderLine


class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

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

    # OrderLine is responsible for calculating its own subtotal. Order is responsible for calculating the overall total.
    def calculate_total(self) -> float:                                      # This method calculates the total cost of the order by iterating through each OrderLine in the order_lines list and summing up their subtotals. It returns a float representing the total amount for the order.
        total: float = 0.0

        for order_line in self.order_lines:                                  # Iterate through each OrderLine in the order_lines list.
            total += order_line.calculate_subtotal()                         # Notice that Order does not calculate each product's price itself. Instead, it delegates the calculation to OrderLine.

        return total                                                         

    def display_order(self) -> None:
        print(f"Order ID: {self.order_id}")

        for order_line in self.order_lines:
            print(
                f"Product: {order_line.product.get_name()}"
            )
            print(
                f"Quantity: {order_line.quantity}"
            )
            print(
                f"Subtotal: ${order_line.calculate_subtotal():.2f}"
            )

        print(f"Total: ${self.calculate_total():.2f}")
