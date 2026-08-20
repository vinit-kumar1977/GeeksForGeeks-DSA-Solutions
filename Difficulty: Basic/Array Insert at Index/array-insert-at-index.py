class Solution:
    def insertAtIndex(self, arr, index, val):
        # code here
        n = len(arr)
        if index >= n:
            arr.append(val)
            return arr
        for i in range(0,len(arr)):
            if i == index:
                arr.insert(i,val)
            
        return arr