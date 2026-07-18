import math as m
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = min(nums)
        y = max(nums)
        xf =[]
        yf=[]
        for i in range(1,int(m.sqrt(x))+1):
            if x % i == 0:
                xf.append(i)
                if i !=  x//i:
                    xf.append(x//i)
        for i in range(1,int(m.sqrt(y))+1):
            if y % i == 0:
                yf.append(i)
                if i !=  y//i:
                    yf.append(y//i)
        common = list(set(xf) & set(yf))
        return(max(common))  
       
        
