import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 존재하지 않는 키를 삽입하려 할때 오류가 발생 -> defaultdict() 사용하여 키 존재 여부를 체크하지 않고 생략
        anagrams = collections.defaultdict(list)
        for word in strs:
            # sorted로 정렬하면 리스트형태로 리턴 -> join()으로 합쳐서 이 값을 키로 하는 딕셔너리로 구성
            # 정렬한 값을 키로하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
solution = Solution()
test_case: List = ["eat","tea","tan","ate","nat","bat"]
result: List[List[str]] = solution.groupAnagrams(test_case)
print(result)
