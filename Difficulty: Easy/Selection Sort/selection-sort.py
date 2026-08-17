class Solution: 
    def selectionSort(self, arr):
        # code here
        for i in range(0,len(arr)-1):
            minimum = i
            for j in range(i,len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
            arr[i],arr[minimum] = arr[minimum],arr[i]
            
        return arr