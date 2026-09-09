class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)

        total = sum(nums)
        selected = []
        current = 0

        for num in nums:
            selected.append(num)
            current += num

            if current > total - current:
                break

        return selected
