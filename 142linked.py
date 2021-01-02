# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = head
        #visited = {}
        while cur != None:
            if cur.next != None and hasattr(cur.next, 'visited'):
                return cur.next
            #setattr(cur, 'visited', True)
            cur.visited = True
            cur = cur.next
        return None


if __name__ == "__main__":
    s = Solution()
    node3 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    nodem4 = ListNode(-4)
    node3.next = node2
    node2.next = node0
    node0.next = nodem4
    nodem4.next = node2
    print(s.detectCycle(node3).val)