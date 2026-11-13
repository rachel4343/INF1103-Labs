from discount_strategy import DiscountStrategy

class NoDiscount(DiscountStrategy):

    def apply(self, total: float) -> float:
        return total                          # It simply returns the original total without applying any discount.
