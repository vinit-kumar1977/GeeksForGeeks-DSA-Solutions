class Solution:
    def minValueToBalance(self, arr: list[int]) -> int:
        # code here
        n = len(arr)
        leftSum = rightSum = 0
        n = n // 2
        for i in range(n):
            leftSum += arr[i]
            rightSum += arr[n+i]
        if leftSum < rightSum:
            return rightSum - leftSum
        else:
            return leftSum - rightSum