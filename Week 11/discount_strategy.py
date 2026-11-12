# This module defines a discount strategy interface and its implementations. It allows for different discount strategies to be applied to an order total.

from abc import ABC, abstractmethod           # ABC allows us to create an abstract base class.

class DiscountStrategy(ABC):

    @abstractmethod                           # Requires subclasses to implement apply(). Every discount strategy must provide its own implementation of apply().
    def apply(self, total: float) -> float:   # The method receives the original order total: total:float.
        pass

# The apply() method is an abstract method that must be implemented by any subclass of DiscountStrategy. It takes a float parameter total, which represents the original order total, and returns a float representing the discounted total. 
# Each discount strategy will have its own implementation of this method, allowing for different discount calculations based on the specific strategy being used.
# Each strategy is responsible for its own discount calculation.
class NoDiscount(DiscountStrategy):

    def apply(self, total: float) -> float:
        return total                          # It simply returns the original total without applying any discount.


class PercentageDiscount(DiscountStrategy):

    def __init__(self, percentage: float):
        self.percentage: float = percentage   

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)  # It calculates the discounted total by multiplying the original total by (1 - percentage/100). For example, if the percentage is 10, it will return 90% of the original total.


class BulkDiscount(DiscountStrategy):

    def __init__(self, threshold: float, amount: float):
        self.threshold: float = threshold
        self.amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:                 # If the total is greater than or equal to the threshold, it applies the discount by subtracting the amount from the total.
            return total - self.amount               

        return total

class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.9  # Apply a 10% discount for students, returning 90% of the original total.