class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for x in nums:
            small_count = 0
            for y in nums:
                if x > y:
                    small_count += 1
            result.append(small_count)
        return result
