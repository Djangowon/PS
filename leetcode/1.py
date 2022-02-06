from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == (nums[i] + nums[j]):
                    return [i,j]


nums = [4,5]
target = 9
print(Solution().twoSum(nums, target))