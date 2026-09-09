class Solution:
    def maxSum(self, nums: list[int]) -> int:
        # Remove duplicate values
        unique = set(nums)

        # If there are positive numbers,
        # take all unique positive numbers.
        positive = [x for x in unique if x > 0]

        if positive:
            return sum(positive)

        # If there are no positive numbers,
        # we must keep at least one element.
        # Choose the largest element.
        return max(nums)
        
