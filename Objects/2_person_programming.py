from __future__ import annotations
from functools import total_ordering
import math
import random

@total_ordering
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
        denominator = self.denominator * other_fraction.denominator
        numerator = self.numerator * (denominator//self.denominator) + other_fraction.numerator * (denominator//other_fraction.denominator)
        return Fraction(numerator, denominator)

    def __sub__(self, other_fraction: Fraction) -> Fraction:
        denominator = self.denominator * other_fraction.denominator
        numerator = self.numerator * (denominator//self.denominator) - other_fraction.numerator * (denominator//other_fraction.denominator)
        return Fraction(numerator, denominator)

    def __eq__(self,other_fraction:Fraction)->Fraction:
        return self.numerator == other_fraction.numerator and self.denominator == other_fraction.denominator
    
    def __gt__(self,other_fraction:Fraction) -> Fraction:
        return (self.numerator/self.denominator) > (other_fraction.numerator/other_fraction.denominator)
    
    def __repr__(self)-> str:
        return f'{self.numerator}/{self.denominator}'

    def __float__(self) -> float:
        return self.numerator / self.denominator


def sortFractions(lst: list[Fraction]) -> list[Fraction]:
    '''
    Given a list of fractions, return the fractions in increasing order
    '''
    for i in range(len(lst)):
        for j in range(len(lst)):
            if float(lst[i]) > float(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst