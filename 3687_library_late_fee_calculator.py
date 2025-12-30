class Solution:
    def lateFee(self, daysLate: list[int]) -> int:
        penalty = 0
        for delay in daysLate:
            if delay == 1:
                penalty += 1
            elif 2 <= delay <= 5:
                penalty += 2 * delay
            else:
                penalty += 3 * delay

        return penalty
