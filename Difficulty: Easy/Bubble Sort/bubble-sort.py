class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)-1
        for i in range(0,n):
            didnotSwap = 0
            for j in range(0,n-i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    didnotSwap = 1
            if didnotSwap == 0:
                break
                    
        return arr