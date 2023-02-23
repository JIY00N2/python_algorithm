from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
       s.reverse()

solution = Solution()
test_case: list = ["h","e","l","l","o"]
result: None = solution.reverseString(test_case)