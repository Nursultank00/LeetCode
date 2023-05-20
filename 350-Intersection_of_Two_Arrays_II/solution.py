# Hashmap 

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
            
        cnt = {}
        for item in nums1:
            cnt[item] = cnt.get(item, 0) + 1
        ans = []
        for x in nums2:
            if x in cnt and cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans