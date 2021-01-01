# Definition for a binary tree node.
from typing import List

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        q = []
        q.append(root)
        res = []

        while len(q) != 0:
            l = len(q)
            tmp = []
            for i in range(l):
                cur = q.pop(0)
                if cur != None:
                    print(cur.val)
                    tmp.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if len(tmp) > 0:
                res.append(tmp)


        return res


if __name__ == "__main__":
    s = Solution()
    print(s.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    #print(s.levelOrder(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
    #print(s.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    #print(s.levelOrder(None))