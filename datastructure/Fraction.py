def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n    


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" +  str(self.den)

    def __add__(self,other):
        num_sum = self.num * other.den + other.num * self.den
        den_sum = self.den * other.den
        return str(num_sum // gcd(num_sum, den_sum)) + "/" + str(den_sum // gcd(num_sum, den_sum))       

    def __sub__(self, other):
        num_sum = self.num * other.den - other.num * self.den
        den_sum = self.den * other.den
        return str(num_sum // gcd(num_sum, den_sum)) + "/" + str(den_sum // gcd(num_sum, den_sum))       

    def __eq__(self, other):
        num_sum1 = self.num * other.den  
        num_sum2 = other.num * self.den
        return num_sum1 == num_sum2

    def  __mul__(self, other):
        num_mul = self.num * other.num
        den_mul = self.den * other.den
        return str(num_mul // gcd(num_mul, den_mul))+ "/" + str(den_mul // gcd(num_mul, den_mul))

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return str( num // gcd(num, den) ) + "/" + str( den // gcd(num, den))

    def __lt__(self, other):
        num_sum1 = self.num * other.den  
        num_sum2 = other.num * self.den
        return num_sum1 - num_sum2 < 0

    def __gt__(self, other):
        num_sum1 = self.num * other.den  
        num_sum2 = other.num * self.den
        return num_sum1 - num_sum2 > 0


 
    
       
