# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        # 빠른 런너와 느린 런너의 초기값은 모두 head에서 시작
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        # next가 존재하지 않을 때까지 이동
        while fast and fast.next:
            # 빠른 런너인 fast는 두 칸씩, 느린 런너 slow는 한 칸씩 이동
            fast = fast.next.next
            # 역순으로 연결 리스트 rev를 생성하는 로직을 slow앞에 덧붙임
            # 역순 연결 리스트는 현재 값을 slow로 교체하고 rev.next는 rev가 된다
            # 즉 앞에 계속 새로운 노드가 추가되는 형태
            rev, rev.next, slow = slow, rev, slow.next
        # 입력값이 홀수일 때와 짝수일 떄 마지막 처리가 다른데
        # 홀수일 때는 slow 런너가 한 칸 더 앞으로 이동하여 중앙의 값을 빗겨 나가야함
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            # 역순으로 만든 연결 리스트 rev를 반복함
            slow, rev = slow.next, rev.next
        return not rev
        # return not slow도 가능

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