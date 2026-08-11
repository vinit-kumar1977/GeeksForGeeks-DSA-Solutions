class Solution:
    def isPower(self, x, y):
        # code here
        counter = 0
        while True:
            if x == 1:
                return False
            power = x**counter
            if power == y:
                return True
            if power > y:
                break
            counter+=1