from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order

# # This script demonstrates the use of various classes and their relationships, including association, aggregation, composition, and polymorphism.
# # Evidence of relationships, LSP and polymorphism
# supplier = Supplier("S001", "TechWorld", "sales@techworld.com")
# laptop = PhysicalProduct("P001", "Laptop", 1000.0, 10, 2.5, supplier)
# ebook = DigitalProduct("P002", "Ebook", 20.0, 50, 15.0, supplier)

# # Aggregation: Inventory stores Product references
# inventory = Inventory()
# inventory.add_product(laptop)
# inventory.add_product(ebook)

# # Polymorphism: Both subclasses work through Product references
# for product in inventory.products:
#     product.display_information()
#     print(product.get_fulfilment_info())

# # Composition: Order creates and manages OrderLine objects
# order = Order("O001")
# order.add_order_line(laptop, 2)
# order.add_order_line(ebook, 1)
# order.display_order()

# # Check that OrderLines are separate objects
# order2 = Order("O002")
# order2.add_order_line(laptop, 1)
# print("Same OrderLine object?", order.order_lines[0] is order2.order_lines[0])

# # Check that both OrderLines refer to the same Product
# print("Same Product object?", order.order_lines[0].product is order2.order_lines[0].product)



# ==========================================
# 1. CREATE SUPPLIER
# ==========================================

supplier = Supplier(
    "S001",
    "TechWorld",
    "sales@techworld.com"
)


# ==========================================
# 2. CREATE PRODUCTS
# ==========================================

laptop = PhysicalProduct(
    "P001",
    "Laptop",
    1000.0,
    10,
    2.5,
    supplier
)

antivirus = DigitalProduct(
    "D001",
    "Antivirus",
    50.0,
    100,
    2.0,
    supplier
)


# ==========================================
# 3. TEST ASSOCIATION
# ==========================================

print("\n===== ASSOCIATION =====")

laptop.supplier.display_information()
antivirus.supplier.display_information()


# ==========================================
# 4. TEST AGGREGATION
# ==========================================

print("\n===== AGGREGATION =====")

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(laptop)
inventory_a.add_product(antivirus)

inventory_a.remove_product("P001")

print("Laptop still exists:", laptop.get_name())

inventory_b.add_product(laptop)

print(
    "Same Product object:",
    inventory_b.find_product("P001") is laptop
)


# ==========================================
# 5. TEST COMPOSITION
# ==========================================

print("\n===== COMPOSITION =====")

order1 = Order("O001")
order2 = Order("O002")

order1.add_order_line(laptop, 2)
order1.add_order_line(antivirus, 3)

order2.add_order_line(laptop, 1)

order1.display_order()
order2.display_order()

print(
    "Same OrderLine:",
    order1.order_lines[0] is order2.order_lines[0]
)

print(
    "Same Product:",
    order1.order_lines[0].product
    is order2.order_lines[0].product
)


# ==========================================
# 6. TEST POLYMORPHISM
# ==========================================

print("\n===== POLYMORPHISM =====")

inventory = Inventory()

inventory.add_product(laptop)
inventory.add_product(antivirus)

for product in inventory.products:
    product.display_information()
    print(product.get_fulfilment_info())


# ==========================================
# 7. TEST FIND PRODUCT
# ==========================================

print("\n===== FIND PRODUCT =====")

found = inventory.find_product("P001")

print("Found:", found is not None)

missing = inventory.find_product("P999")

print("Missing:", missing is None)