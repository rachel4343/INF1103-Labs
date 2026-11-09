# This code defines a class named Supplier that represents a supplier entity. The class has three attributes: supplier_id, name, and contact_email, all of which are expected to be strings. 

class Supplier:
    # This creates an instance attribute and annotates its intended type.
    # The __init__ method initializes the Supplier object with the provided attributes: supplier_id, name, and contact_email. 
    # The type hints indicate that these attributes are expected to be strings. Type hints are used to provide additional information about the expected types of variables, function parameters, and return values. 
    # Type hints help improve code readability, facilitate static type checking, and assist developers in understanding the intended usage of the code. However, they do not enforce type checking at runtime.
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.supplier_id: str = supplier_id                               # This creates an instance attribute and annotates its intended type.
        self.name: str = name
        self.contact_email: str = contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.supplier_id}")
        print(f"Supplier Name: {self.name}")
        print(f"Contact Email: {self.contact_email}")
