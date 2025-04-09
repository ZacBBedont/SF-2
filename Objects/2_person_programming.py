from __future__ import annotations
import math

class Fraction:
    def __init__(self,numerator=0,denominator=1):
        if denominator == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        if numerator/denominator > 0:
            sign = 1
        else:
            sign = -1
        gcd = math.gcd(numerator, denominator)
        self.denominator = abs(denominator) // gcd
        self.numerator = abs(numerator) // gcd * sign

    def __add__(self, other_fraction: Fraction) -> Fraction:
        added_f = Fraction(self.numerator, self.denominator)
        added_f.numerator *= other_fraction.denominator
        added_f.denominator *= other_fraction.denominator
        added_f.numerator += other_fraction.numerator*self.denominator
        return added_f

    def __sub__(self, other_fraction: Fraction) -> Fraction:
        subbed_f = Fraction(self.numerator, self.denominator)
        subbed_f.numerator *= other_fraction.denominator
        subbed_f.denominator *= other_fraction.denominator
        subbed_f.numerator -= other_fraction.numerator*self.denominator
        return Fraction(subbed_f.numerator, subbed_f.denominator)

f1 = Fraction(10, 3)
f2 = Fraction(6, -2)
result = f1 - f2
print(result.numerator, result.denominator)
            


