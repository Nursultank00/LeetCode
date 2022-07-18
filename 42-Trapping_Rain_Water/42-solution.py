class Solution:
    def trap(self, height: List[int]) -> int:
        max_index = height.index(max(height))
        ans = 0
        nowm = 0
        for i in range(max_index):
            if nowm < height[i]:
                nowm = height[i]
            ans += nowm - height[i]
        nowm = 0
        for i in range(len(height)-1,max_index,-1):
            if nowm < height[i]:
                nowm = height[i]
            ans += nowm - height[i]
        return ans