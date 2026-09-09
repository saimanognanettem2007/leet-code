class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}

        # Count frequency of each letter
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        # Sort frequencies from highest to lowest
        frequencies = sorted(freq.values(), reverse=True)

        ans = 0

        for i in range(len(frequencies)):
            pushes = (i // 8) + 1
            ans += frequencies[i] * pushes

        return ans
