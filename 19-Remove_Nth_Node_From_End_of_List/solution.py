# Два поинтера, одним проходимся n раз, дальше запускаем обоих

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = ListNode(0)
        first.next = second = head
        result = first
        while n > 0:
            second = second.next
            n -= 1
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return result.next