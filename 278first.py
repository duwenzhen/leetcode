# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    v = 1
    def isBadVersion(self, num):
        return self.v <= num

    def helper(self, first, last):
        if first == last:
            return first
        else:
            m = (first + last) // 2
            if self.isBadVersion(m):
                return self.helper(first,m)
            else:
                return self.helper(m + 1, last)

    def firstBadVersion(self, n):
        return self.helper(0, n)

sol = Solution()
print(sol.firstBadVersion(1))