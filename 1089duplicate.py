from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        initlen = len(arr)
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                i = i + 1
            i = i + 1
        dif = len(arr) - initlen
        for i in range(dif):
            del arr[-1]




s = Solution()
arr = [8,4,5,0,0,0,0,7]
s.duplicateZeros(arr)
print(arr)

arr = [0,1,7,6,0,2,0,7]
s.duplicateZeros(arr)
print(arr)

arr = [1,0,2,3,0,4,5,0]
s.duplicateZeros(arr)
print(arr)

arr = [1,2,3]
s.duplicateZeros(arr)
print(arr)

arr = [1]
s.duplicateZeros(arr)
print(arr)

arr = [0]
s.duplicateZeros(arr)
print(arr)

arr = [0,0]
s.duplicateZeros(arr)
print(arr)