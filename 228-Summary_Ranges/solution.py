# Два поинтера, смотрим на следующий элемент

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        pointer = 0
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                continue
            elif pointer == i:
                ans.append(str(nums[i]))
            else:
                ans.append(str(nums[pointer])+"->"+str(nums[i]))
            pointer = i + 1
        
        return ans