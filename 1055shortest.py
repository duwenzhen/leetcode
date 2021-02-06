class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        i = 0
        count = 1

        for char in target:
            i = source.find(char, i)
            if i == -1:
                i = source.find(char)
                count += 1
                if i == -1:
                    return i
            i += 1

        return count
s = Solution()
print(s.shortestWay("xyz", "xzyxz"))

print(s.shortestWay("abc", "abcbc"))
print(s.shortestWay("abc", "acdbc"))
