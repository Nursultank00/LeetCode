# бинарный поиск с условиями

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if nums[right] >= nums[mid] and nums[right] < target:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[left] <= nums[mid] and nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1