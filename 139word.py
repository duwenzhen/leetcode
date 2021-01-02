from typing import List

class Solution:




    def rec(self, str, wordDict):
        if str in self.done:
            return self.done[str]
        if len(str) == 0:
            return True
        res = False
        for w in wordDict:

            if str.startswith(w):
                res = res or self.rec(str[len(w):], wordDict)
        self.done[str] = res
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.done = {}
        return self.rec(s, wordDict)



if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(sol.wordBreak(s, wordDict))
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(sol.wordBreak(s, wordDict))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(sol.wordBreak(s, wordDict))
