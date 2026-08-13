class Solution:
    def rotate(self, arr):
        n = len(arr)
        def rotateArr(startIdx,endIdx):
            while startIdx < endIdx:
                arr[startIdx],arr[endIdx] = arr[endIdx],arr[startIdx]
                startIdx += 1
                endIdx -= 1
        rotateArr(0,n-2)
        rotateArr(0,n-1)
        return arr