class Solution:
    def getSecondLargest(self, arr):
        # code here
        fLarge = sLarge = 0
        for num in arr:
            if num > fLarge:
                sLarge = fLarge
                fLarge = num
            elif num > sLarge and num < fLarge:
                sLarge = num
        if sLarge == 0:
            sLarge = -1
        return sLarge