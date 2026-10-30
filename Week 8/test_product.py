from product import Product

product1 = Product("P001", "Laptop", 1200.00, 15)

product1.display_information()

print("\nUpdating stock...\n")

product1.update_stock(20)

product1.display_information()