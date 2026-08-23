class Solution:
    def segregate0and1(self, arr):
        # code here
        n = len(arr)
        counter = 0
        for i in range(n):
            if arr[i] == 0:
                arr[counter] = 0
                counter += 1
                
        while counter < n:
            arr[counter] = 1
            counter += 1
            
        return arr