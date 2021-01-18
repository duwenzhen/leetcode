# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:


    def recRun(self, root, level):
        if root == None:
            return
        else:
            print(root.val, level)
            if level not in self.sums:
                self.sums[level] = root.val
            else:
                self.sums[level] += root.val
            if root.left:
                self.recRun(root.left, level +1)
            if root.right:
                self.recRun(root.right, level +1)



    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.sums = {}
        self.recRun(root, 1)
        levelnb = len(self.sums)
        return self.sums[levelnb]



s = Solution()
print(s.deepestLeavesSum(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, right=TreeNode(6, right=TreeNode(8))))))
print(s.deepestLeavesSum(TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, right=TreeNode(5))))))
#s.recRun(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, right=TreeNode(6, right=TreeNode(8)))))