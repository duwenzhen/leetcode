from typing import List

class Solution:


    def rec(self, candidates, target, l:List[int], results):
        if sum(l) > target:
            return
        if sum(l)  == target:
            l.sort()
            if l not in results:
                print(l)

                results.append(l)
                print(results)
            return

        for i in candidates:
            nl = l.copy()
            nl.append(i)
            self.rec(candidates, target, nl, results)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        print(candidates)
        results = []
        self.rec(candidates, target, [], results)
        return results


if __name__ == "__main__":
    s = Solution()
    candidates = [2,3,5]
    target = 8
    print(s.combinationSum(candidates, target))