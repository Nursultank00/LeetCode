# Словарь и линейный обход, добавляем в словарь target-num, ищем num 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target-nums[i]]=i