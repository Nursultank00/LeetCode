# Считаем префиксную сумму, берём остаток по k, прибавляем к результату то, что в словаре

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0:1}
        presum = 0
        result = 0
        for item in nums:
            presum += item
            presum %= k
            if presum in d:
                result += d[presum]
            d[presum] = d.get(presum, 0) + 1
        return result