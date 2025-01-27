def isDistinct(year: int) -> bool:
    s = str(year)
    digits_used = []
    for char in s:
        if char in digits_used:
            return False
        digits_used.append(char)
    return True
year = int(input("Please put in a year")) + 1
while not isDistinct(year):
    year += 1