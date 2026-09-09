class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        # Count each character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        length = 0
        odd = False

        # Calculate the palindrome length
        for value in count.values():
            length += (value // 2) * 2

            if value % 2 == 1:
                odd = True

        # One odd character can be placed in the middle
        if odd:
            length += 1

        return length
