#todo redo it again.

class Solution(object):

    #official solution
    def numTrees(self, n):
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)

if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(2))
    print(s.numTrees(3))
    print(s.numTrees(4))
    print(s.numTrees(5))