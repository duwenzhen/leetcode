class Solution:
    translated = {'1':'1', '6':'9', '8':'8', '0':'0', '9':'6'}

    def isStrobogrammatic(self, num: str) -> bool:
        first = 0
        last = len(num) - 1

        while first <= last:
            if num[first] in self.translated and num[last] in self.translated:
                if self.translated[num[first]] != num[last]:
                    return False
                first += 1
                last -= 1
            else:
                return False
        return True

s = Solution()
print(s.isStrobogrammatic("69"))
print(s.isStrobogrammatic("88"))
print(s.isStrobogrammatic("962"))
print(s.isStrobogrammatic("1"))
print(s.isStrobogrammatic("101"))
print(s.isStrobogrammatic("61019"))
print(s.isStrobogrammatic("0"))