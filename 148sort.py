# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:

    def findthemid(self, head: ListNode):
        cur = head
        mid = head
        prevmid = None
        while cur!= None and cur.next != None:
            cur = cur.next.next
            prevmid = mid
            mid = mid.next

        prevmid.next = None
        return mid


    def merge(self, left, right):
        curleft = left
        curright = right

        if curleft.val < curright.val:
            head = curleft
            curleft = curleft.next
        else:
            head = curright
            curright = curright.next

        cur = head
        while curright != None or curleft != None:
            if curright == None:
                cur.next = curleft
                curleft = curleft.next
                cur = cur.next
            elif curleft == None:
                cur.next = curright
                curright = curright.next
                cur = cur.next
            else:
                if curleft.val < curright.val:
                    cur.next = curleft
                    curleft = curleft.next
                    cur = cur.next
                else:
                    cur.next = curright
                    curright = curright.next
                    cur = cur.next

        return head



    def rec(self, head: ListNode):
        if head == None or head.next == None:
            return head
        mid = self.findthemid(head)
        left = self.rec(head)
        right = self.rec(mid)
        return self.merge(left, right)


    def sortList(self, head: ListNode) -> ListNode:
        return self.rec(head)


if __name__ == "__main__":
    s = Solution()
    #head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    res = s.sortList(head)
    print(res.val)

