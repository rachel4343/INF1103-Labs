
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

# # 2. Implement association: Supplier and Product
# # 1. Create Supplier independently
# supplier1 = Supplier(
#     "S001",
#     "TechWorld",
#     "sales@techworld.com"
# )

# # 2. Create products using the SAME Supplier
# physical = PhysicalProduct(
#     "P001",
#     "Laptop",
#     1000.0,
#     10,
#     2.5,
#     supplier1
# )

# digital = DigitalProduct(
#     "D001",
#     "Antivirus Software",
#     50.0,
#     100,
#     2.0,
#     supplier1
# )

# # 3. Delete the original supplier variable
# del supplier1

# # 4. Access Supplier through each Product
# print("Physical Product Supplier:")
# physical.supplier.display_information()

# print("\nDigital Product Supplier:")
# digital.supplier.display_information()

# # 5. Confirm both Products share the SAME Supplier object
# print("\nAre they associated with the same Supplier?")
# print(physical.supplier is digital.supplier)


# 3. Implement aggregation: Inventory and Product
# 1. Create Supplier independently
supplier1 = Supplier(
    "S001",
    "TechWorld",
    "sales@techworld.com"
)

# 2. Create Product BEFORE Inventory
laptop = PhysicalProduct(
    "P001",
    "Laptop",
    1000.0,
    10,
    2.5,
    supplier1
)

# 3. Create two inventories
inventory_a = Inventory()
inventory_b = Inventory()

# 4. Add laptop to Inventory A
inventory_a.add_product(laptop)

print("Laptop in Inventory A:")
found_product = inventory_a.find_product("P001")

if found_product is not None:
    found_product.display_information()

# 5. Remove laptop from Inventory A
inventory_a.remove_product("P001")

print("\nAfter removing Laptop from Inventory A:")
print("Laptop name:", laptop.get_name())  # Confirm Laptop object still exists

# Confirm Inventory A no longer contains Laptop
print("Found in Inventory A:", inventory_a.find_product("P001"))



# 6. Add the SAME object to Inventory B
inventory_b.add_product(laptop)

print("\nLaptop in Inventory B:")
found_product = inventory_b.find_product("P001")

if found_product is not None:
    found_product.display_information()

# 7. Confirm it is the SAME object
print("\nIs it the same Product object?")
print(laptop is inventory_b.find_product("P001"))
