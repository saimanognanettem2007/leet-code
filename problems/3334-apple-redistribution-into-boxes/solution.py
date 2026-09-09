class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total_apples = sum(apple)

        capacity.sort(reverse=True)

        total_capacity = 0

        for i in range(len(capacity)):
            total_capacity += capacity[i]

            if total_capacity >= total_apples:
                return i + 1

        return len(capacity)
