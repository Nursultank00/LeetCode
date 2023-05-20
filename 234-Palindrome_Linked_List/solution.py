# Находим середину, и реверсим оставшуюся часть

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        hair = tortoise = head
        while hair and hair.next:
            hair = hair.next.next
            tortoise = tortoise.next
        mid = tortoise
        prev = None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True