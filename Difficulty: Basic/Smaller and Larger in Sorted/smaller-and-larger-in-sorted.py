class Solution:
    def getMoreAndLess(self, arr, target):
        # code here
        lessNum = greaterNum = 0
        for num in arr:
            if num == target:
                lessNum += 1
                greaterNum += 1
            if num < target:
                lessNum += 1
            elif num > target:
                greaterNum += 1
        return [lessNum,greaterNum]