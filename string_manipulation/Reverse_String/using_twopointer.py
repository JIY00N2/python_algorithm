from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

solution = Solution()
test_case: list = ["h","e","l","l","o"]
result: None = solution.reverseString(test_case)