from product import Product
from inventory import Inventory


inventory = Inventory()

product1 = Product("P001", "Laptop", 1200.00, 15)
product2 = Product("P002", "Mouse", 25.50, 40)

inventory.add_product(product1)
inventory.add_product(product2)

print("=== ALL PRODUCTS ===")
inventory.display_all()

print("=== SEARCH ===")

result = inventory.search_product("P002")

if result:
    result.display_information()
else:
    print("Product not found.")