class Solution:
    def sortInWave(self, arr):
        # code here
        
        i ,j = 0,1
        n = len(arr)
        while j <= n-1:
            arr[i],arr[j] = arr[j],arr[i]
            i+=2
            j+=2
        return arr