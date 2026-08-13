class Solution:
    def countOfElements(self, x, arr):
        # code here
        counter = 0
        for num in arr:
            if num <= x:
                counter+=1
        return counter
