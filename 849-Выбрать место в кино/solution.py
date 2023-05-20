# два указателя - три случая

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        result = 0
        left = 0
        for right in range(len(seats)):
            if seats[right] == 1:
                if left == 0 and seats[left] == 0:
                    result = max(result, right-left)
                else:
                    result = max(result, (right-left)//2)
                left = right
            elif right == len(seats)-1:
                result = max(result, right-left)
        return result