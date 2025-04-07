int1 = input()
int2 = input()
try:
    print(int(int1)/int(int2))
except ValueError:
    print("ooh im sorry did you do a whoopsie?")