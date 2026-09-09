import heapq

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        # Python has a min heap, so use negative values
        heap = [-x for x in nums]
        heapq.heapify(heap)

        score = 0

        for _ in range(k):
            m = -heapq.heappop(heap)

            score += m

            heapq.heappush(heap, -(m + 1))

        return score
