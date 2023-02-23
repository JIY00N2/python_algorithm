# using deque O(n)
import collections
from typing import Deque

class Solution:
    def isPalindrome(self, s:str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop(): # popleft() - 원소 제거
                return False
        return True

solution = Solution()
test_case: str = "race a car"
result: bool = solution.isPalindrome(test_case)
print(result)

