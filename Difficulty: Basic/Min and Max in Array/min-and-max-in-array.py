class Solution:
    def getMinMax(self, arr):
        # code here
        minNumber = float('inf')
        maxNumber = -float('inf')
        for num in arr:
            if num > maxNumber:
                maxNumber = num
            if num < minNumber:
                minNumber = num
        return [minNumber,maxNumber]