from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List =[]
        if not head:
            return True
        node = head
        # 리스트로 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0)!=q.pop():
                return False
        return True

solution = Solution()
if __name__ == "__main__":
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(2)
    list4 = ListNode(1)
    head = list1
    list1.next = list2
    list2.next = list3
    list3.next = list4

result: bool = solution.isPalindrome(head)
print(result)