# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isValidBSTRec(self, root: TreeNode, mini, maxi) -> bool:
        if root == None:
            return True
        elif root.val <= mini or root.val >= maxi:
            return False
        else:
            leftres = True
            rightres = True
            if root.left != None:
                if root.left.val < root.val:
                    leftres = self.isValidBSTRec(root.left, mini, min(root.val, maxi))
                else:
                    leftres = False
            if root.right != None :
                if root.right.val > root.val:
                    rightres  = self.isValidBSTRec(root.right, max(mini, root.val), maxi)
                else:
                    rightres = False
            return leftres and rightres
    l = []
    def toArray(self, root: TreeNode):
        if root == None:
            return
        else:
            self.toArray(root.left)
            self.l.append(root.val)
            self.toArray(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self.l = []
        #return self.isValidBSTRec(root,  -pow(2,32), pow(2,32)-1)
        self.toArray(root)
        i = 1
        while i < len(self.l):
            if (self.l[i] <= self.l[i - 1]):
                return False
            i = i + 1
        return True





if __name__ == "__main__":
    s = Solution()
    print(s.isValidBST(TreeNode(1, TreeNode(1))))
    print(s.isValidBST(TreeNode(0)))
    print(s.isValidBST(TreeNode(-2147483648)))
    print(s.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))

    print(s.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))))
    print(s.isValidBST(TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))))