class Solution:
    def find(self, arr, x):
        # code here
        firstOccur = lastOccur = -1
        for i in range(len(arr)):
            if firstOccur == -1 and arr[i] == x:
                firstOccur = i
                lastOccur = i
            elif arr[i] == x:
                lastOccur = i
                
        return [firstOccur,lastOccur]