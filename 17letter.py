mapping = {'0': [],
           '1' : [],
           '2' : ['a', 'b', 'c'],
           '3' : ['d','e','f'],
           '4' : ['g','h','i'],
           '5' : ['j','k','l'],
           '6' : ['m','n','o'],
           '7' : ['p','q','r', 's'],
           '8' : ['t','u','v'],
           '9' : ['w','x','y', 'z']}

from typing import List

class Solution:
    def combi(self, x, y):
        res = []
        for i in x:
            for j in y:
                res.append(i+j)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or len(digits) > 4:
            return []
        help = []
        for d in digits:
            help.append(mapping[d])

        res = help[0]
        i = 1
        while i < len(digits):
            res = self.combi(res, help[i])
            i = i + 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))