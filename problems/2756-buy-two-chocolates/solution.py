class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()

        total = prices[0] + prices[1]

        if total <= money:
            return money - total

        return money
