# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None

        def inorder(node):
            # --- 递归终止条件 ---
            # 1. 如果节点为空，说明走到了叶子节点的边界，返回
            # 2. 如果 self.res 已经有值，说明已经找到了目标，提前结束递归（剪枝）
            if not node or self.res is not None:
                return
            #我们必须先尽可能向左走，直到触底，才能保证是从最小的元素开始计数的
            inorder(node.left)
            # 当从左子树回溯回来时，说明当前节点是剩余节点中最小的
            self.count += 1

            if self.count == k:
                self.res = node.val
                return # 找到后立即返回，不再继续遍历
            inorder(node.right)

        inorder(root)
        return self.res
