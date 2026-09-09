class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int,
                         energy: list[int], experience: list[int]) -> int:

        hours = 0

        for i in range(len(energy)):

            # Need more energy
            if initialEnergy <= energy[i]:
                needed = energy[i] + 1 - initialEnergy
                hours += needed
                initialEnergy += needed

            # Need more experience
            if initialExperience <= experience[i]:
                needed = experience[i] + 1 - initialExperience
                hours += needed
                initialExperience += needed

            # Defeat opponent
            initialEnergy -= energy[i]
            initialExperience += experience[i]

        return hours
