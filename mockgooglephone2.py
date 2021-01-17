from typing import List

class Solution:
    def divisors(self, n):
        res = []
        i = 1
        while i <= n:
            if (n % i == 0):
                res.append(i)
            i = i + 1
        return res

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dict_count = {}
        for v in deck:
            if v not in dict_count:
                dict_count[v] = 0
            dict_count[v] = dict_count[v] + 1
        dict_div = {}
        for k,v in dict_count.items():
            if v < 2:
                return False
            divisors = self.divisors(v)
            for d in divisors:
                if d not in dict_div:
                    dict_div[d] = 0
                dict_div[d] += 1

        for k,n in dict_div.items():
            if k > 1 and n == len(dict_count):
                return True

        return False



s = Solution()
print(s.hasGroupsSizeX([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]))
print(s.hasGroupsSizeX([1,2,3,4,4,3,2,1]))
print(s.hasGroupsSizeX([1,1,1,2,2,2,3,3]))
print(s.hasGroupsSizeX([1]))
print(s.hasGroupsSizeX([1,1]))
print(s.hasGroupsSizeX([1,1,2,2,2,2]))
print(s.hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))
