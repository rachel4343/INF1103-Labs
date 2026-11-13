from discount_strategy import DiscountStrategy

class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.9  # Apply a 10% discount for students, returning 90% of the original total.