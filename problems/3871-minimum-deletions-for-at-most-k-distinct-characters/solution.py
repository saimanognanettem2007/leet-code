class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        # Count frequency of each character
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Number of distinct characters
        distinct = len(freq)

        # Already at most k distinct characters
        if distinct <= k:
            return 0

        # We need to remove the characters
        # having the smallest frequencies
        frequencies = sorted(freq.values())

        deletions = 0
        remove = distinct - k

        for i in range(remove):
            deletions += frequencies[i]

        return deletions
        
