n, m, d = input().split()
n,m,d = int(n),int(m),int(d)
times,dirty = 0,0
events = [int(x) for x in input().split()]
for day in range(1,d+1):
    if dirty == n:
        times += 1
        dirty = 0
    dirty += 1
    for x in events:
        if x == day:
            n += 1
print(times)