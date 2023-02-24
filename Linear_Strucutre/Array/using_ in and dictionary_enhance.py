# O(1) ~ O(n)
# using in and dictionary 개선
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map= {}
        # 하나의 for문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i

solution = Solution()
nums:  list = [2,7,11,15]
target: int = 9
result: list = solution.twoSum(nums, target)
print(result)