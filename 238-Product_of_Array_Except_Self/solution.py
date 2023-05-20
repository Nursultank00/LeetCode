# Считаем пресуммы обходя список с двух сторон, обновляем один из них умножением

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        revers = [1]*n
        for i in range(1,n):
            result[i] = result[i-1] * nums[i-1]
        
        for j in range(n-2, -1, -1):
            revers[j] = revers[j+1]*nums[j+1]
        
        for i in range(n):
            result[i] = result[i] * revers[i]
        return result
