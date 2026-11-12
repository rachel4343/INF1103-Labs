from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from discount_strategy import BulkDiscount, PercentageDiscount, StudentDiscount
from product_factory import ProductFactory

supplier = Supplier("S001", "TechWorld", "sales@techworld.com")

product = PhysicalProduct("P001", "Laptop", 125.0, 10, 2.5, supplier)

# Create an order with a bulk discount
order = Order("O001", BulkDiscount(200, 20))

# Add 2 laptops ($125 x 2 = $250)
order.add_order_line(product, 2)
print("Bulk Discount:", order.calculate_total())

# Change the discount strategy
order.set_discount(PercentageDiscount(10))
print("Percentage Discount:", order.calculate_total())

# Change the discount strategy to student discount
order.set_discount(StudentDiscount())
print("Student Discount:", order.calculate_total())


# Testing the ProductFactory class:
# supplier = Supplier("S001", "TechWorld", "sales@techworld.com")
# ProductFactory.create("physical", "P001", "Laptop", 125.0, 10, supplier, weight=2.5)
# ProductFactory.create("digital", "P002", "Software", 50.0, 100, supplier, download_size=500.0)
# ProductFactory.create("service", "P003", "Installation", 100.0, 10, supplier)  # This line will raise a ValueError because "service" is not a recognized product type in the ProductFactory. The factory method only supports "physical" and "digital" product types, so attempting to create a product with an unrecognized type will trigger the error handling mechanism defined in the create method.


# print("Program started")

# supplier = Supplier(
#     "S001",
#     "TechWorld",
#     "sales@techworld.com"
# )

# ProductFactory.create(
#     "physical",
#     "P001",
#     "Laptop",
#     125.0,
#     10,
#     supplier,
#     weight=2.5
# )

# print("Physical product created")

# ProductFactory.create(
#     "service",
#     "P003",
#     "Installation",
#     100.0,
#     10,
#     supplier
# )

# print("Program finished") # never executes because Python terminates the program when the unhandled exception occurs.


print("Program started")

supplier = Supplier(
    "S001",
    "TechWorld",
    "sales@techworld.com"
)

try:
    ProductFactory.create(
        "service",
        "P003",
        "Installation",
        100.0,
        10,
        supplier
    )

except ValueError as e:      # Catch the ValueError raised by the ProductFactory.create method when an unrecognized product type is provided. This allows the program to handle the error gracefully without terminating unexpectedly, providing an opportunity to log or display an error message to inform the user about the issue with the input parameters.
    print(f"Error: {e}")     # e is a variable that stores the exception object. Print the error message associated with the caught ValueError, providing feedback to the user or developer about the specific issue that occurred during the product creation process. This helps in diagnosing problems and understanding why the product creation failed.


print("Program finished")
