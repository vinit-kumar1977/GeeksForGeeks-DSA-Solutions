class Solution:
    def getAlternates(self, arr):
        # Code Here
        finalArr = []
        for i in range(0,len(arr),2):
            finalArr.append(arr[i])
            
        return finalArr