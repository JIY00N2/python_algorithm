# O(n^2)
# 브르투 포스는 Time Out
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort() # 정렬 먼저
        for i in range(len(nums) -2):
            # 중복된 값 건너뛰기 투 포인터가 같은 값
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1 # left는 i 한칸 옆, right는 맨 뒤 정렬해서 왼쪽은 음수, 오른쪽은 양수
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else: # sum = 0 인경우
                    results.append([nums[i], nums[left], nums[right]])
                    # 정답 추가한 다음에 left, right 양 옆으로 동일한 값이 있을 수 있으므로 이를 left+=1, right-=1을 반복해서 스킵 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 마지막으로 left를 한칸 우측으로, right를 왼쪽으로 더 이동하고 다음으로 넘김
                    left += 1
                    right -= 1

        return results

solution = Solution()
nums:  list = [-1, 0, 1, 2, -1, -4]
result: list[list] = solution.threeSum(nums)
print(result)