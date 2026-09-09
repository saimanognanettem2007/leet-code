class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # Maximum value
        max_num = s

        for ch in s:
            if ch != '9':
                max_num = s.replace(ch, '9')
                break

        # Minimum value
        min_num = s

        for ch in s:
            if ch != '0':
                min_num = s.replace(ch, '0')
                break

        return int(max_num) - int(min_num)
