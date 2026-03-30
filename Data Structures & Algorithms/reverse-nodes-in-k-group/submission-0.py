# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for _ in range(k):
            if not curr: return head
            curr = curr.next
        new_head = self.reverse(head, curr)
        head.next = self.reverseKGroup(curr, k)
        return new_head

    def reverse(self,first, last):
        prev, curr = None, first
        while curr != last:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        





