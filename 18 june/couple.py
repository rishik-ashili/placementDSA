class Solution:
    def findSingle(self, arr):
        result = 0
        for num in arr:
            result ^= num
        return result