
from discount_strategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):

    def __init__(self, threshold: float, amount: float):
        self.threshold: float = threshold
        self.amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:                 # If the total is greater than or equal to the threshold, it applies the discount by subtracting the amount from the total.
            return total - self.amount               

        return total
