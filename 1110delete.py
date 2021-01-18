
from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = {}
        parent = {}
        res[root.val] = root
        parent[root.val] = None
        fifo = []
        fifo.append(root)
        while len(fifo) > 0:
            current = fifo[0]
            del fifo[0]
            if current.val in to_delete:
                if current.left:
                    res[current.left.val] = current.left
                if current.right:
                    res[current.right.val] = current.right
            if current.left:
                fifo.append(current.left)
                parent[current.left.val] = current
            if current.right:
                fifo.append(current.right)
                parent[current.right.val] = current

        for d in to_delete:
            if d in res:
                del res[d]
            if d in parent:
                p = parent[d]
                if p:
                    if p.right and p.right.val == d:
                        p.right = None
                    if p.left and p.left.val == d:
                        p.left = None
        return list(res.values())


s = Solution()
print(s.delNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))), [3,5]))
print(s.delNodes(TreeNode(1), [3,5]))
print(s.delNodes(TreeNode(1), []))