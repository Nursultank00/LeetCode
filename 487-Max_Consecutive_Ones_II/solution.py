def f(nums):
    result = 0
    left = 0
    zeroes = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes += 1
        while zeroes > 1:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        result = max(result, i - left+1)
    return result