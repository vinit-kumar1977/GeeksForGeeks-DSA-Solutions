class Solution:
    def reverseArray(self, arr):
        # code here
        j = len(arr)-1
        for i in range(0,len(arr)//2):
            
            arr[i],arr[j] = arr[j],arr[i]
            j-=1
        return arr
        
        