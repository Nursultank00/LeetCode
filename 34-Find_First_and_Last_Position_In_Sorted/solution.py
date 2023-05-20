# Находим левый конец бинарным поиском, находим правый, если левый больше правого - [-1,-1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        ansleft, ansright = 0, n-1
        while ansleft <= right:
            mid = (ansleft+right)//2
            if nums[mid] < target:
                ansleft = mid + 1
            else:
                right = mid - 1
        
        while left <= ansright:
            mid = (left + ansright)//2
            if nums[mid] > target:
                ansright = mid - 1
            else:
                left = mid + 1
        return [ansleft, ansright] if ansleft <= ansright else [-1, -1]