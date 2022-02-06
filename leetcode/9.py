import self as self


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True


x = -121
print(Solution.isPalindrome(self, x))