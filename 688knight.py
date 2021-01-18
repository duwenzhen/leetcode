'''import random

class Solution:
    move = [(-1, 2),(1, 2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1)]
    def isOut(self, x, y, n):
        return x < 0 or x >= n or y < 0 or y >= n

    def randomMove(self):
        return random.randint(0, 7)


    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        n = 100000000
        res = 0.0
        for i in range(n):
            x = r
            y = c
            out = False
            for k in range(K):
                nextmove = self.randomMove()
                x = x + self.move[nextmove][0]
                y = y + self.move[nextmove][1]
                if self.isOut(x,y,N):
                    out = True
                    break
            if not out:
                res += 1.0
        return res / n

'''

class Solution:
    move = [(-1, 2),(1, 2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1)]
    def isOut(self, x, y, n):
        return x < 0 or x >= n or y < 0 or y >= n

    def help(self, N, K, r, c):
        if self.isOut(r,c, N):
            return 0
        if K == 0:
            return 1
        if (r,c,K) in self.memo:
            return self.memo[(r,c,K)]
        sum = 0.0
        for i in range(8):
            sum += self.help(N, K-1, r + self.move[i][0], c + self.move[i][1])
        self.memo[(r,c,K)] = sum * 0.125
        return sum * 0.125

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        self.memo = {}
        return self.help(N, K, r,c)




s = Solution()
print(s.knightProbability(3,2,0,0))