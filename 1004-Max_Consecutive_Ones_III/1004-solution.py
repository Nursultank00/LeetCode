class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = []
        current_streak = 0
        longest_streak = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                current_streak += 1
            else:
                if len(zeros) == k:
                    zeros.append(i)
                    last_zero = zeros.pop(0)
                    current_streak = i - last_zero
                else:
                    current_streak += 1
                    zeros.append(i)
                    
            longest_streak = max(longest_streak, current_streak)
        
        return longest_streak