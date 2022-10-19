#First solution
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = maxlen = zerocount = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zerocount += 1
            
            while zerocount > 1:
                if nums[left] == 0:
                    zerocount -= 1
                left += 1
                
            maxlen = max(maxlen, right - left)
        
        return maxlen

#Second solution
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        prev = curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
                longest = max(longest, prev + curr)
            else:
                prev, curr = curr, 0
        return longest - (longest == len(nums))