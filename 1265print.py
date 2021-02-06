# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
class ImmutableListNode:
     def printValue(self) -> None: # print the value of this node.
         pass
     def getNext(self) -> ImmutableListNode: # return the next node.
         return  None

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        cur = head
        stack = []
        while cur != None:
            stack.append(cur)
            cur = cur.getNext()

        while len(stack) > 0:
            stack.pop().printValue()

