"""
find all divisors of an integer n that is not 0
"""

def divisors(n):
    divisors = []
    for i in range(1,abs(n)+1):
        if n%i == 0:
            divisors.append(i)
            divisors.append(-1*i)
    return divisors

valid = False
while not valid:
    s = input("enter password")
    valid = (len(s) == 6 and s[:3] == "app")

"""
output = ?

A. Whatsapp
B. Apples
C. Abcapp
D. apples
E. both Band D
F. Both C and D
G. NOne of the above
"""