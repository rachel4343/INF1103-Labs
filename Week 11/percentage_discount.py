from discount_strategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):

    def __init__(self, percentage: float):
        self.percentage: float = percentage   

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)  # It calculates the discounted total by multiplying the original total by (1 - percentage/100). For example, if the percentage is 10, it will return 90% of the original total.

