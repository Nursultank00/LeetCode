# Два указателя, один на последнем нуле, другой текущий

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        current = last = 0
        while current < n:
            cur = nums[current]
            l = nums[last]
            if cur != 0 and l != 0:
                current += 1
                last += 1
                continue
            if cur != 0 and l == 0:
                nums[last] = cur
                nums[current] = 0
                last += 1
            current += 1