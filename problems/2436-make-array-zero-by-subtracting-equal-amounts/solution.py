class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count = 0
        values = []

        for num in nums:
            if num != 0 and num not in values:
                values.append(num)
                count += 1

        return count
