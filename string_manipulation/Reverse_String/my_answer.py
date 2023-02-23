from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s = s[::-1]도 맞긴 하지만 오류
        # 공간복잡도 O(1) 때문에 s[:] = s[::-1] 로 작성
        s[:] = s[::-1]

solution = Solution()
test_case: list = ["h", "e", "l", "l", "o"]
result: None = solution.reverseString(test_case)