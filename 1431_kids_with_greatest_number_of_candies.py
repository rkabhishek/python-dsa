class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        result = [candy + extraCandies >= maxCandies for candy in candies]
        return result
