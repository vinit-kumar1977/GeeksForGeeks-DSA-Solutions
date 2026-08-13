class Solution:
    def isPalinArray(self, arr):
         # code here
        def checkNumberPalindrom(num):
            copyVal = num
            rev = 0
            while num > 0:
                rem = num % 10
                rev = rev * 10 + rem
                num = num // 10
            if copyVal == rev:
                return True
            else:
                return False
        for num in arr:
            if not checkNumberPalindrom(num):
                return False
        return True
            