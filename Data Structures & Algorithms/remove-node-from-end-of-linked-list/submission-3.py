# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #处理删除头节点的情况
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
        #curr重新指向dummy
        curr = dummy

        for i in range(length - n):
            curr = curr.next
            
        curr.next = curr.next.next
        return dummy.next