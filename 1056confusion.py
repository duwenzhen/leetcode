class Solution:
    def confusingNumber(self, N: int) -> bool:
        dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        s = str(N)
        res = ""
        for c in s:
            if c not in dic:
                return False
            else:
                res = dic[c] + res
        return int(res) != N

s = Solution()
print(s.confusingNumber(1))
print(s.confusingNumber(0))
print(s.confusingNumber(6))
print(s.confusingNumber(89))
print(s.confusingNumber(11))
print(s.confusingNumber(25))



