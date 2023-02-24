from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        pair = []

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

solution = Solution()
nums:  list = [1,4,3,2]
result: int = solution.arrayPairSum(nums)
print(result)