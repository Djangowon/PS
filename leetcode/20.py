from self import self

s = str(input())


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}':'{',')':'(',']':'['}
        stack = []
        for i in s:
            if i in brackets.values():
                stack.append(i)
            else:
                if stack and brackets[i] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True


print(Solution.isValid(self, s))
