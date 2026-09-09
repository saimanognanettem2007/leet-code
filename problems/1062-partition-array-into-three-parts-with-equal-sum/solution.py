class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)

        # Total must be divisible by 3
        if total % 3 != 0:
            return False

        target = total // 3
        count = 0
        current_sum = 0

        for i in range(len(arr)):
            current_sum += arr[i]

            if current_sum == target:
                count += 1
                current_sum = 0

        return count >= 3
