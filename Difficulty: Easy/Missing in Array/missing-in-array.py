class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr)+1
        total = (n*(n+1))//2
        sum = 0
        for num in arr:
            sum += num
        return total-sum
            
        