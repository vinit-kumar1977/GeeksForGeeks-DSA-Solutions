class Solution:
    def removeDuplicates(self, arr):
        # code here 
        for i in range(len(arr)-1,0,-1):
            if arr[i] == arr[i-1]:
                del arr[i]
        return arr
        