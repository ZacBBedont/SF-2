"""
Firgus is behind on several assignments.
After rummaging through his backpack he realizes that he has n items each of which he records as strings
he has M upcoming assignments, the i-th of which requires T_i items to complete, r1,r2 ... rT_i
if he has T_i required items, he can complete thge assignment. Otherwise he flunks.
How many assignments can Firgus complete

INPUT:
first line contains 2 integres n and m separated by a space
next n line contain a single string s_i
    you can assume that the n strings are unique
next m sections contain a single integer T_i followed by T_i line each containing a single string

OUTPUT:
output the number of assignments Firgus can complete

EX:
Input:
3 4
chalk
cheese
charger
1
cheese
2
coins
cash
3
charger
chalk
caffeine
3
cheese
charger
chalk
Output:
2
"""
n,m = input().split()
n,m = int(n), int(m)
items = set()
count = 0
for _ in range(n):
    items.add(input())
for _ in range(m):
    required_no = int(input())
    required = set()
    for _ in range(required_no):
        required.add(input())
    required.update(items)
    if required == items:
        count += 1
print(count)