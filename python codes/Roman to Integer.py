class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        prev = 0
        tot = 0
        for i in s:
            tot += roman[i]
            if roman[i] > prev:
                tot -= 2*prev
            prev = roman[i]
        return tot

        
