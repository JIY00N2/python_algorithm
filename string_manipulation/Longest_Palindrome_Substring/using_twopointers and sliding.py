class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        # 해당 사항이 없을때 파르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 오른쪽으로 이동
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i,i+2), key=len) # max(str, key = len): 문자열의 길이가 가장 큰 것 반환
            return result

solution = Solution()
test_case:  str = "babad"
result: str = solution.longestPalindrome(test_case)
print(result)