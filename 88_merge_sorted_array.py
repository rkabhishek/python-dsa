class Solution:
    def mergeCombinedSort(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:m+n] = nums2
        nums1.sort()

    def mergeUsingTempList(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        temp = nums1[:m]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if temp[i] < nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1


        while i < m:
            nums1[k] = temp[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
