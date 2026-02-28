class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if ch.isalnum())

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].upper() != s[right].upper():
                return False

            left += 1
            right -= 1

        return True
