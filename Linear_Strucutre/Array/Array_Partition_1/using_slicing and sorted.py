from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2]) # [::2]는 두칸씩 건너뛰므로 짝수 번째 계산

solution = Solution()
nums:  list = [1,4,3,2]
result: int = solution.arrayPairSum(nums)
print(result)