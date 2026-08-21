class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        totalFine = 0
        for i in range(len(car)):
            if date & 1:
                if car[i] % 2 == 0:
                    totalFine += fine[i]
            else:
                if car[i] % 2 == 1:
                    totalFine += fine[i]
                    
        return totalFine
                    
    
    