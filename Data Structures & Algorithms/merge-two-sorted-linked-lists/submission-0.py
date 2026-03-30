# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 创建一个伪节点作为起始点
        dummy = ListNode()
        # 2. 用 curr 指针来负责“串联”工作，dummy 保持在原地不动
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            # 记得移动 curr 指针到新挂上去的节点上
            curr = curr.next

        # 3. 循环结束后，处理还没走完的那个链表
        curr.next = list1 if list1 else list2

        # 4. 返回 dummy.next（即真正的头节点）
        return dummy.next

