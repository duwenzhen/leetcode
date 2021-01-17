
def guess(val):
    c = 2
    if val == c:
        return 0
    if val < c:
        return 1
    else:
        return -1

class Solution:
    def guessrec(self, low, high):
        mid = (low + high) // 2
        res = guess(mid)
        if res == 0:
            return mid
        else:
            if res == -1:
                return self.guessrec(low-1, mid)
            else:
                return self.guessrec(mid, high+1)

    def guessNumber(self, n: int) -> int:
        return self.guessrec(1, n)


s = Solution()
print(s.guessNumber(2))