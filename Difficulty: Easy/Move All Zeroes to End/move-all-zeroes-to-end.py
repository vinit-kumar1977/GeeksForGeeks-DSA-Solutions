class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	counter = 0
    	for i in arr:
    	    if i != 0:
    	        arr[counter] = i
    	        counter+=1
    	        
    	while counter<len(arr):
    	    arr[counter] = 0
    	    counter+=1
    	return arr