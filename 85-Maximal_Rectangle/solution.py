# The stack maintain the indexes of buildings with ascending height. 
# Before adding a new building pop the building who is taller than the new one. 
# The building popped out represent the height of a rectangle 
# with the new building as the right boundary and the current 
# stack top as the left boundary. Calculate its area and update ans of maximum area.
#  Boundary is handled using dummy buildings.

def maximalRectangle(self, matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0
    for row in matrix:
        for i in range(n):
            height[i] = height[i] + 1 if row[i] == '1' else 0
        stack = [-1]
        for i in range(n + 1):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h * w)
            stack.append(i)
    return ans