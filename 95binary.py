# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rec(self, root: TreeNode, res):
        if root == None:
            return


        self.rec(root.left, res)
        res.append(root.val)
        self.rec(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.rec(root, res)
        return res




if __name__ == "__main__":
    s = Solution()
    s.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None)))