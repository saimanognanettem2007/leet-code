class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # Take as many 1s as possible
        take_ones = min(k, numOnes)
        k -= take_ones

        # 1 contributes +1
        ans = take_ones

        # Take zeros next
        take_zeros = min(k, numZeros)
        k -= take_zeros

        # 0 contributes nothing

        # Remaining items must be -1
        ans -= k

        return ans
