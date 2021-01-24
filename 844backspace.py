class Solution:
    def help(self, s):
        res = ""
        count = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                count += 1
            else:
                if count > 0:
                    count = count - 1
                else:
                    res = s[i] + res
            i -= 1
        return res


    def backspaceCompare(self, S: str, T: str) -> bool:
        s = self.help(S)
        t = self.help(T)
        return s == t



s = Solution()
print(s.backspaceCompare(S = "ab#c", T = "ad#c"))
print(s.backspaceCompare(S = "ab##", T = "c#d#"))
print(s.backspaceCompare(S = "a##c", T = "#a#c"))
print(s.backspaceCompare(S = "a#c", T = "b"))
print(s.backspaceCompare(S = "a", T = "#"))
print(s.backspaceCompare(S = "#", T = "#"))