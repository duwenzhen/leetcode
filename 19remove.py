# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        helper = []
        cur = head
        while cur != None:
            helper.append(cur)
            cur = cur.next

        idx = len(helper) - n
        if idx == 0:
            return helper[idx].next
        helper[idx - 1].next = helper[idx].next
        return head

if __name__ == "__main__":
    s = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = ListNode(1)
    print(s.removeNthFromEnd(l,1))

