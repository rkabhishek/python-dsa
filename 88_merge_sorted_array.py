class Solution:
    def mergeCombinedSort(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:m+n] = nums2
        nums1.sort()
