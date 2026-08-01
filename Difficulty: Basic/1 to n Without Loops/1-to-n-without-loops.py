class Solution:
    
    def printTillN(self, n):
    	#code here 
    	numbers = []
    	def printNumber(num):
            if num == 0:
                return
            printNumber(num-1)
            numbers.append(num)
        
        printNumber(n)

    	print(*numbers,end =' ')
    	