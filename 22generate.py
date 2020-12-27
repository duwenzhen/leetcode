mapping =['(',')']

from typing import List

class Solution:
    def combi(self, x, y):
        res = []
        for i in x:
            for j in y:
                res.append(i+j)
        return res

    def valid(self, c):
        res = 0
        for i in c:
            if i == "(":
                res = res + 1
            else:
                res = res -1
            if res < 0:
                return False

        return res == 0

    def generateParenthesis1(self, n) -> List[str]:
        if n == 0 or n > 8:
            return []

        res = mapping
        i = 1
        while i < n*2:
            res = self.combi(res, mapping)
            i = i + 1
        resres = []
        for r in res:
            if self.valid(r):
                resres.append(r)
        return resres

    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def bt(s: str, op: int, cl: int):  # op = opened parentheses, cl = closed parentheses
            if len(s) == n * 2:
                out.append(s)
                return

            if op < n:
                bt(s + "(", op + 1, cl)

            if op > cl:
                bt(s + ")", op, cl + 1)

        bt("", 0, 0)

        return out


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))