from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while start <= end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1

s = Solution()
st = ["h","e","l","l","o"]
s.reverseString(st)
print(st)

st = ["h","e","3","l","o", "5"]
s.reverseString(st)
print(st)

st = []
s.reverseString(st)
print(st)

st = ["5"]
s.reverseString(st)
print(st)

st = [""]
s.reverseString(st)
print(st)