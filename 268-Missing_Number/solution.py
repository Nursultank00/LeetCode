# XOR manipulation or check sum

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i, value in enumerate(nums):
            result ^= i + 1
            result ^= value
        return result