# using slicing
import re
class Solutions:
    def isPalindrome(self,s : str) -> bool:
        s = s.lower()
        # 정규 표현식 re.sub: 문자열 치환
        # re.sub(정규표현식, 치환문자, 대상 문자열)
        # ^ 문자열의 시작을 의미
        s = re.sub('[^a-z0-9]','',s)
        # [::-1] 역순 출력
        return s == s[::-1] # slicing
solutions = Solutions()
test_case: str = "race a car"
result: bool = solutions.isPalindrome(test_case)
print(result)