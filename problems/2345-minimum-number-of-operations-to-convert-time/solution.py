class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_hour = int(current[:2])
        current_minute = int(current[3:])

        correct_hour = int(correct[:2])
        correct_minute = int(correct[3:])

        current_total = current_hour * 60 + current_minute
        correct_total = correct_hour * 60 + correct_minute

        difference = correct_total - current_total

        operations = 0

        for x in [60, 15, 5, 1]:
            operations += difference // x
            difference %= x

        return operations
