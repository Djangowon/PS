import time

import self as self

start_time = time.time()


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True


x = -121
print(Solution.isPalindrome(self, x))


end_time = time.time()
print("time :", end_time - start_time)