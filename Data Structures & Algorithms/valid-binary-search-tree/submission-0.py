# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(curr, low, high):
            if not curr:
                return True
            #不用if low < curr.val < high，因为不能根据当前节点满足条件就判定整棵树满足
            if not low < curr.val < high:
                return False
            return valid(curr.left, low, curr.val) and valid(curr.right, curr.val, high)
        return valid(root, float('-inf'),float('inf'))
        