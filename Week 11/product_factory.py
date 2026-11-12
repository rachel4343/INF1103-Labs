from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


class ProductFactory:

    @staticmethod  # This decorator indicates that the create method is a static method, meaning it can be called on the class itself without needing an instance of the class. This is appropriate for a factory method, as it doesn't rely on any instance-specific data and is used to create new product instances based on the provided parameters.
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier,
        weight: float = 0.0,
        download_size: float = 0.0
    ) -> Product:

        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, weight, supplier)

        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, download_size, supplier)

        else:
            raise ValueError(f"Unknown product type: {product_type}")  # Raise a ValueError if the provided product_type is not recognized, indicating that the factory method cannot create a product of the specified type. This helps to catch errors early and provides clear feedback to the caller about the issue with the input parameters.