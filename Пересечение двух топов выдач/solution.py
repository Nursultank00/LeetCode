def DoIt(arr1, arr2):
    result = []
    count = 0
    hasht1 = {}
    hasht2 = {}
    n = len(arr1)
    for i in range(n):
        if arr1[i] == arr2[i]:
            count += 1
        else:
            hasht1[arr1[i]] = hasht1.get(arr1[i], 0) + 1
            hasht2[arr2[i]] = hasht2.get(arr2[i], 0) + 1
            if arr1[i] in hasht2 and hasht2[arr1[i]] > 0:
                count += 1 
                hasht2[arr1[i]] -= 1
            if arr2[i] in hasht1 and hasht1[arr2[i]] > 0:
                count += 1 
                hasht1[arr2[i]] -= 1
        result.append(count)
    return result

assert(DoIt([1,2,3,4], [2,0,1,3]) == [0, 1, 2, 3])