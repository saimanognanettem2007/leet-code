class Solution:
    def minTimeToType(self, word: str) -> int:
        current = 'a'
        time = 0

        for ch in word:
            diff = abs(ord(ch) - ord(current))

            # Minimum distance in the circle
            time += min(diff, 26 - diff)

            # Type the character
            time += 1

            current = ch

        return time
