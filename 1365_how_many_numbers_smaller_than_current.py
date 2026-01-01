class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for x in nums:
            small_count = sum(1 for y in nums if x > y)
            result.append(small_count)
        return result

    def smallerNumbersThanCurrentUsingSort(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        smaller_than_map = {}
        for i in range(len(sorted_nums)):
            num = sorted_nums[i]
            if num not in smaller_than_map:
                smaller_than_map[num] = i

        result = []
        for i in range(len(nums)):
            count = smaller_than_map[nums[i]]
            result.append(count)

        return result

