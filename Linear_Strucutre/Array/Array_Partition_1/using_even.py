from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i, n in enumerate(nums):
            # 짝수 번째에는 항상 작은 값이 존재하므로 짝수 값 더하기
            if i % 2 == 0:
                sum += n

        return sum

solution = Solution()
nums:  list = [1,4,3,2]
result: int = solution.arrayPairSum(nums)
print(result)