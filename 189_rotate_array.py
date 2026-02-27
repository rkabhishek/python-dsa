class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        result = []
        for i in range(n - k, n):
            result.append(nums[i])

        for i in range(n - k):
            result.append(nums[i])

        nums[:] = result
