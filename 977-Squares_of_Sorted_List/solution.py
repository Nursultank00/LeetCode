# Два указателя справа и слева, сжимаем их

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        while nums:
            left = nums[0]**2
            right = nums[-1]**2
            if left > right:
                result.append(left)
                nums.pop(0)
            else:
                result.append(right)
                nums.pop()
        return result[::-1]