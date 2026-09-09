class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > 9 * n:
            return -1

        if s == 0:
            return 0

        result = ""

        for i in range(n):
            digit = min(9, s)
            result += str(digit)
            s -= digit

        return int(result)
