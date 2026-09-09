class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        answer = 0

        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    answer = max(answer, j - i)

        return answer
