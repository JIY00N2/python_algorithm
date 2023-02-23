# 팰린드롬 = 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장
# using list O(n^2)
# -> : 반환 값의 자료형 표시
# 콜론(:): 매개변수의 자료형 표시
# 풀이 1: 리스트로 변환
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for c in s:
            if c.isalnum():
                strs.append(c.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

solution = Solution()
test_case: str = "race a car"
result: bool = solution.isPalindrome(test_case)
print(result)
