import collections
from typing import List, Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    	# 전처리 - 정규표현식 + 소문자 변경 + banned 거르기
        # \w: 단어 문자, ^: not -> 문자가 아닌 문자를 공백으로 치환
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                if word not in banned]
        # Counter 객체를 이용하여 가장 높은 빈도의 문자 찾기
        counts = collections.Counter(words)
        # most_common(1) -> [('ball',2)] 리스트
        # most_common(1)[0] -> ('ball',2) 튜플
        # most_common(1)[0][0] -> ball 튜플 첫번째 값
        return counts.most_common(1)[0][0]

solution = Solution()
# test_case 1
paragraph: str= "Bob hit a ball, the hit BALL flew far after it was hit."
# test_case 2
banned: List[str] = ["hit"]