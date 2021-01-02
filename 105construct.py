# Definition for a binary tree node.
from typing import List

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rec(self, preorder: List[int], inorder: List[int]) -> TreeNode:


        if len(preorder) == 0:
            return None

        root = preorder[0]
        if len(preorder) == 1:
            return TreeNode(root)
        indexOfRoot = inorder.index(root)
        left = inorder[:indexOfRoot]
        right = inorder[indexOfRoot + 1:]
        left_preorder = preorder[1:indexOfRoot+1]
        right_preorder = preorder[indexOfRoot+1:]
        return TreeNode(root, self.rec(left_preorder, left), self.rec(right_preorder, right))




    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.rec(preorder, inorder)
if __name__ == "__main__":
    s = Solution()
    s.buildTree([3,9,20,15,7], [9,3,15,20,7])