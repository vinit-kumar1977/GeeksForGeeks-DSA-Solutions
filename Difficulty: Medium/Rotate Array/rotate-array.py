class Solution:
    def rotateArr(self, arr, d):
        # code here
        n = len(arr)
        d = d % n
        def reverseArr(startIdx,endIdx):
            while endIdx > startIdx:
                temp = arr[startIdx]
                arr[startIdx] = arr[endIdx]
                arr[endIdx] = temp
                startIdx += 1
                endIdx-=1
            return arr
        reverseArr(0,d-1)
        reverseArr(d,n-1)
        reverseArr(0,n-1)
        
        return arr