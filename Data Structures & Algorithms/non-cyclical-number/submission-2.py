class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        newNum = n
        while (newNum != 1): #fill in later
            newNum = self.parseThrough(newNum)
            if newNum in seen:
                return False
            else:
                seen.add(newNum)
            print(newNum)
        return True
            

    def parseThrough(self, n):
        sumOfDigits = 0
        while n > 0:
            currentDigit = n % 10
            sumOfDigits += currentDigit ** 2
            n //= 10
        return sumOfDigits


    

        