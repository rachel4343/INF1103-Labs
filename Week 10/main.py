
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# 1. Create Supplier independently
supplier1 = Supplier(
    "S001",
    "TechWorld",
    "sales@techworld.com"
)

# 2. Create products using the SAME Supplier
physical = PhysicalProduct(
    "P001",
    "Laptop",
    1000.0,
    10,
    2.5,
    supplier1
)

digital = DigitalProduct(
    "D001",
    "Antivirus Software",
    50.0,
    100,
    2.0,
    supplier1
)

# 3. Delete the original supplier variable
del supplier1

# 4. Access Supplier through each Product
print("Physical Product Supplier:")
physical.supplier.display_information()

print("\nDigital Product Supplier:")
digital.supplier.display_information()

# 5. Confirm both Products share the SAME Supplier object
print("\nAre they associated with the same Supplier?")
print(physical.supplier is digital.supplier)
