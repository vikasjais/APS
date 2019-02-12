def maximumSum(a):
    maxSum = tMaxSum = 0
    for i in a:
        tMaxSum += i
        if tMaxSum < 0:
            tMaxSum = 0
        if maxSum < tMaxSum:
            maxSum = tMaxSum
    return maxSum

print(maximumSum([-2,-3,4,-1,-2,1,5,-3]))
