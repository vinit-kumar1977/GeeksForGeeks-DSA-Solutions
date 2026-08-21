class Solution:
    def multiply(self, arr):
        # Code here
        n = len(arr)
        k = n // 2
        n = k
        if len(arr) & 1:
            n += 1
        leftSum = rightSum = 0
        for i in range(0,n):
            if i < k:
                leftSum += arr[i]
            index = n + i
            if n != k:
                index -= 1
            rightSum += arr[index] if index < len(arr) else 0
            
        return leftSum * rightSum
                
            
        
            