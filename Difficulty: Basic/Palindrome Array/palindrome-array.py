class Solution:
    def isPalindrome(self, arr):
        # code here
        n = len(arr)
        for i in range(0,n):
            if arr[i] != arr[n-i-1]:
                return False
        return True
            
