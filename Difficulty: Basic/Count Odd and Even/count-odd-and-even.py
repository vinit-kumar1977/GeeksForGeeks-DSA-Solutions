class Solution:
	def countOddEven(self, arr):
		#Code here
		evenCount = oddCount = 0
		for num in arr:
		    if num & 1:
		        oddCount += 1
		    else:
		        evenCount += 1
		        
        return [oddCount,evenCount]
		        
		        