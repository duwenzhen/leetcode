class Solution:

    def rec(self, m, n, done):
        if (m,n) in done:
            return done[(m,n)]
        if m == 1 and n == 1:
            return 1
        if m == 0:
            return 0

        if n == 0:
            return 0
        count = self.rec(m-1, n, done)  + self.rec(m, n-1, done)
        done[(m,n)] = count
        return count

    def uniquePaths(self, m: int, n: int) -> int:
        done = {}

        return self.rec(m, n, done)


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(23,12))