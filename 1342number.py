class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num -1

            count = count + 1

        return count


s = Solution()
print(s.numberOfSteps(14))
print(s.numberOfSteps(8))
print(s.numberOfSteps(123))
print(s.numberOfSteps(0))
