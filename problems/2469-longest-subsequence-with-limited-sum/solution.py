class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()

        # Prefix sums
        prefix = []
        total = 0

        for num in nums:
            total += num
            prefix.append(total)

        answer = []

        for q in queries:
            count = 0

            for total in prefix:
                if total <= q:
                    count += 1
                else:
                    break

            answer.append(count)

        return answer
