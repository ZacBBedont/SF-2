class Fraction:
    def __init__(self,numerator=0,denominator=1):
        if denominator == 0:
            raise ZeroDivisionError('Cannot divide by zero')
f1 = Fraction()
f2 = Fraction(3,7)
