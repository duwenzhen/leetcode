
# Definition for a Node.
class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node):
        if head == None:
            return None
        cur = head
        prev = None

        dic = {}
        while cur != None:
            new = Node(cur.val)
            dic[cur] = new
            if prev != None:
                prev.next = new
            prev = new
            cur = cur.next
        cur = head
        newcur = dic[head]
        while cur != None:
            if cur.random != None:
                newcur.random = dic[cur.random]
            cur = cur.next
            newcur = newcur.next
        return dic[head]

if __name__ == "__main__":
    s = Solution()
    node7 = Node(7)
    node13 = Node(13)
    node11 = Node(11)
    node10 = Node(10)
    node1 = Node(1)
    node7.next = node13
    node7.random = None
    node13.next = node11
    node13.random = node7
    node11.next = node10
    node11.random = node1
    node10.next = node1
    node10.random = node11
    node1.next = None
    node1.random = node7


    s.copyRandomList(node7)
