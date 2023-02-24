# O(n^2) not good
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i,j]
                    return result

solution = Solution()
nums:  list = [2,7,11,15]
target: int = 9
result: list = solution.twoSum(nums, target)
print(result)