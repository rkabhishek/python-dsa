class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        result = []
        result.extend(nums[n-k:])
        result.extend(nums[:n-k])

        nums[:] = result

    def rotate_(self, nums: list[int], k: int) -> None:
        n = len(nums)
        self._reverse_range(nums, 0, n - k - 1)
        self._reverse_range(nums, n - k, n - 1)
        self._reverse_range(nums, 0, n - 1)


    def _reverse_range(self, nums: list[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
