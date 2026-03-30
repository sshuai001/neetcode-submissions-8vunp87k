# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #边界情况：都为空，说明这一分支匹配成功
        if not p and not q:
            return True
        #如果其中一个为空
        if not p or not q:
            return False
        #如果值不相同
        if p.val != q.val:
            return False
        # 必须左边完全一样 (p.left == q.left) 且 右边完全一样 (p.right == q.right)
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
