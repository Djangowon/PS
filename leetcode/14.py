from typing import List

from self import self

strs = list(map(str, input().split()))


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        res = ''
        strs = sorted(strs)
        for i in strs[0]:
            if strs[-1].startswith(res + i):
                res += i
            else:
                break
        return res


print(Solution.longestCommonPrefix(self, strs))

