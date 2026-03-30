# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟头节点，作为新链表的起点
        dummy = ListNode(0)
        curr = dummy  
        carry = 0     # 进位信息，必须定义在循环外
        
        # 只要 l1 没走完，或者 l2 没走完，或者最后还有一个进位没填
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            
            carry = total // 10    # 取整除，得到进位 (0 或 1)
            new_val = total % 10   # 取余数，得到当前位的值
            
            # 创建新节点并连接到结果链表上
            curr.next = ListNode(new_val)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next



