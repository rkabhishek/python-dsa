class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        result = []
        result.extend(nums[n-k:])
        result.extend(nums[:n-k])

        nums[:] = result
