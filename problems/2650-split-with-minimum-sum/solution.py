class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))

        num1 = 0
        num2 = 0

        for i in range(len(digits)):
            if i % 2 == 0:
                num1 = num1 * 10 + int(digits[i])
            else:
                num2 = num2 * 10 + int(digits[i])

        return num1 + num2
