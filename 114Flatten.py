# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def recFlatten(self, node,  resNode):
        if node == None:
            return
        else:
            cur = resNode
            while cur.right != None:
                cur = cur.right
            cur.right = TreeNode(node.val)
            self.recFlatten(node.left, resNode)
            self.recFlatten(node.right, resNode)


    def initTree(self):
        return TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, right=TreeNode(6)))

    def flatten(self, root: TreeNode) -> None:
        resNode = TreeNode(0)
        self.recFlatten(root, resNode)
        root = resNode.right




if __name__ == "__main__":
    s = Solution()
    s.flatten(s.initTree())
