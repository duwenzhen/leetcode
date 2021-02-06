from typing import List

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        nl = []
        for i, v in enumerate(indexes):
            nl.append((v, sources[i], targets[i]))

        nl = sorted(nl, key=lambda x: x[0], reverse=True)

        for i,s,t in nl:
            l = len(s)
            if S[i:i + l] == s:
                S = S[:i] + t + S[i + l:]
        return S

s = Solution()
print(s.findReplaceString(S = "vmokgggqzp", indexes = [3,5,1], sources = ["kg","ggq","mo"], targets = ["s","so","bfr"]))

print(s.findReplaceString(S = "abcd", indexes = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]))
print(s.findReplaceString(S = "abcd", indexes = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]))
