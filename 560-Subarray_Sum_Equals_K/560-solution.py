class Solution:
    def subarraySum(self, nums, k) -> int:
        presum = 0
        d = {0:1}
        answer = 0
        
        for i in nums:
            presum = presum + i
            
            if presum - k in d:
                answer = answer + d[presum-k]
                
            d[presum] = d.get(presum, 0) + 1
        
        return answer