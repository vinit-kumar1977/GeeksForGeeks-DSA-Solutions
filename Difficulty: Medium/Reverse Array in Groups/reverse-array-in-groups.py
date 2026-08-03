class Solution:

    def reverseInGroups(self, arr, k):
        """code here"""
        if k == 1: return arr
        
        def rotate(start,end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            
        n = len(arr)
        
        if n <= k:
            rotate(0,n-1)
            return arr
            
        for i in range(0,n,k):
            start = i
            end = min(i+k-1,n-1)
            rotate(start,end)
            
        return arr
            
        
        