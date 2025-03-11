"""
There are many ways to write e-mail adresses.
--> take a gmail address and add a + and a string before the @ sign and the email adress is still valid
    ex: louisa.harutyunyan@gmail.com = 
        louisa.harutyunyan+helloworld@gmail.com
--> dots before the @symbol are also ignored
    ex: louisa.harutyunyan@gmail.com = 
        lou.is.a.har.ut.yunya.n@gmail.com
--> uppercase and lowercase differences are ignored
    ex: louisa.harutyunyan@gmail.com = 
        lOuIsa.hArutYuNyan@gmail.com
given emnail adresses given by the user, determine the number of them that are unique
rules of email adresses are above
INPUT:
--> first line contains integer n(amount of email addresses)
--> next n lines: email adresses
    at least one character before @ symbol, which consist of: letters,numbers,dots and plusses
--> characters after the @ symbol consist of letter,numbers and dots
OUTPUT:
number of unique email adresses
"""
#TODO: Read input from user
#TODO: clean email addresses
#TODO: collect clean addresses in a list
#TODO: return the amount of unique addresses
def clean(address):
    address.lower()
    at_pos = address.find("@")
    plus_pos = address.find("+")
    if plus_pos != -1:
        address = address[:plus_pos]+ address[at_pos:]
        at_pos = address.find("@")
    address = address[:at_pos].replace(".","") + address[at_pos:]
    address.lower()
    return address
    
    
n = int(input())
addresses = set()
for _ in range(n):
    address = input()
    address = clean(address)
    addresses.add(address)
print(len(addresses))