# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval*2):   # merge 0 with 1, 2 with 3, 4 with 5
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])  # then merge 0 with 2, 4 with 6, ...
            interval *= 2
        return lists[0] if k > 0 else None
    
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next