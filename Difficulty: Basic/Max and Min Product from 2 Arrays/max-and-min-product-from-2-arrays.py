

class Solution:
    
    def minMaxProduct(self, arr1, arr2):
        # code here
        min = float('inf')
        max = float('-inf')
        for num in arr1:
            if num > max:
                max = num
        for num in arr2:
            if num < min:
                min = num
        return min * max
            
            