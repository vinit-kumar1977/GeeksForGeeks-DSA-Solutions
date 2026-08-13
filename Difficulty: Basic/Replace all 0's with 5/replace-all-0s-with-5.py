class Solution:
    def convertFive(self, n):
        # code here
        if n == 0:
            return 5
        rev = 0
        while n > 0:
            rem = n % 10
            if rem == 0:
                rem = 5
            rev = rev * 10 + rem
            n = n // 10
            
        reverse = 0
        while rev > 0:
            rem = rev % 10
            reverse = reverse * 10 + rem
            rev = rev // 10
        return reverse
            
            