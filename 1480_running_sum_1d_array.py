class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        running = 0
        for num in nums:
            running += num
            ans.append(running)

        return ans
