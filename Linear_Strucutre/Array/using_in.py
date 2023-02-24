# O(n)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n  # 타켓에서 첫번째 값을 뺀 값을 찾기
            if complement in nums[i+1:]: # 현재 반복 이후 값들로 이루어진 리스트에서 비교
                # 현재 반복 이후 리스트에서 비교했으니 (i + 1)을 더해 입력 리스트의 인덱스를 추출
                return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]

solution = Solution()
nums:  list = [2,7,11,15]
target: int = 9
result: list = solution.twoSum(nums, target)
print(result)