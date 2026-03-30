# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
        curr = dummy # 停留在待删除节点的前一个节点，还能处理删除head节点的情况
        #倒数第n个=>正数第length - n个
        for _ in range(length - n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
