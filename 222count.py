# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        if root.left == None and root.right == None:
            return 1
        else:
            lefty = 0
            if root.left:
                lefty = self.countNodes(root.left)
            righty = 0
            if root.right:
                righty = self.countNodes(root.right)
        return lefty + righty + 1

