# This module defines a discount strategy interface and its implementations. It allows for different discount strategies to be applied to an order total.

from abc import ABC, abstractmethod           # ABC allows us to create an abstract base class.

class DiscountStrategy(ABC):

    @abstractmethod                           # Requires subclasses to implement apply(). Every discount strategy must provide its own implementation of apply().
    def apply(self, total: float) -> float:   # The method receives the original order total: total:float.
        pass

# The apply() method is an abstract method that must be implemented by any subclass of DiscountStrategy. It takes a float parameter total, which represents the original order total, and returns a float representing the discounted total. 
# Each discount strategy will have its own implementation of this method, allowing for different discount calculations based on the specific strategy being used.
# Each strategy is responsible for its own discount calculation.