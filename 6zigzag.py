
'''
1 5 9 13
2 4 6 8 10 12 14
3 7 11



1 7 13
2 6 8 12 14
3 5  9 11
4 10
'''

s = "AB"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = [''] * numRows
        idx = 0
        i = 0
        inc = True

        for i in range(len(s)):
            res[idx] = res[idx] + s[i]
            if inc:
                idx = idx + 1
            else:
                idx = idx - 1
            if idx == numRows - 1 or idx == 0:
                inc = not inc
        return ''.join(res)




if __name__ == "__main__":
    sol = Solution()
    print(sol.convert(s,1))


