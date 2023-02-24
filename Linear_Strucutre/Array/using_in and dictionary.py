# O(1) ~ O(n)
from typing import List
# target에서 첫 번째 수를 빼면 두 번째 수를 바로 알아낼 수 있다.
# 그렇다면 두 번째 수를 key로 하고 기존의 index를 value로 바꿔서 dictionary에 저장해두면,
# 나중에 두 번째 수를 key로 조회해서 정답을 즉시 찾아낼 수 있다.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} # key: value
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타켓에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i !=nums_map[target-num]:
                return [i, nums_map[target-num]]


solution = Solution()
nums:  list = [2,7,11,15]
target: int = 9
result: list = solution.twoSum(nums, target)
print(result)