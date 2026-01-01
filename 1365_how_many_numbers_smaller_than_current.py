class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for x in nums:
            small_count = sum(1 for y in nums if x > y)
            result.append(small_count)
        return result
