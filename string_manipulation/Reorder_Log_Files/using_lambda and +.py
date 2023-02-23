from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit(): # isdigit - 숫자 여부
                digits.append(log)
            else:
                letters.append(log)
        # sort - 리턴 x, sorted - 정렬된 새로운 리스트 리턴
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # key = lambda : key값에 함수를 넘겨주면 우선순위 정렬
        return letters + digits
        # letters + digits : letters 다음에 digits
solution = Solution()
logs: List = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
result: List = solution.reorderLogFiles(logs)
print(result)