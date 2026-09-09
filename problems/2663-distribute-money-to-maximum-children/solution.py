class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # Give every child $1 first
        money -= children

        if money < 0:
            return -1

        # Each child needs 7 more dollars to reach $8
        count = min(money // 7, children)
        money -= count * 7

        # All children got $8
        if count == children:
            if money > 0:
                return children - 1
            return children

        # If remaining money makes one child have $4
        if count == children - 1 and money == 3:
            return count - 1

        return count
