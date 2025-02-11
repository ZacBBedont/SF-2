bonuses = 0
total1 = 0
total2 = 0
lst = []
f,d = input().split()
f,d = int(f), int(d)
for x in range(d):
    listsmall = list(map(int,input().split()))
    lst.append(listsmall)
for i in range(f):
    for x in range(d):
        total1 += lst[x][i]
    if total1 % 13 == 0:
        bonuses += total1 // 13
    total1 = 0
for i in range(d):
    for x in range(f):
        total2 += lst[x][i]
    if total2 % 13 == 0:
        bonuses += total2 // 13
print(bonuses)

