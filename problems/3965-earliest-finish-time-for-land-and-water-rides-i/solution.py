class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int],
                           waterStartTime: list[int], waterDuration: list[int]) -> int:

        answer = float('inf')

        # Land ride first, then water ride
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_start = max(land_finish, waterStartTime[j])
                finish = water_start + waterDuration[j]

                answer = min(answer, finish)

        # Water ride first, then land ride
        for j in range(len(waterStartTime)):
            water_finish = waterStartTime[j] + waterDuration[j]

            for i in range(len(landStartTime)):
                land_start = max(water_finish, landStartTime[i])
                finish = land_start + landDuration[i]

                answer = min(answer, finish)

        return answer
