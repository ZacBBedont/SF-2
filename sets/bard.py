"""
Every evening villagers gather round and sing songs

if the bard is present, he sings a new song that no villager knows
if the bard is not present, every villager present shares songs

given a list of villagers present for E consecutive evenings, output villagers that know every song from that period

INPUT:
--> int N, no of villagers
--> int E, no of evenings
--> next E lines: each line starts with K no of villagers, followed by K + integers representing villager number id. all separated by spaces

no villager will appear twice per night and the bard will appear at least once in the nights
villager no. 1 is the bard

OUTPUT:
output all villager no id that know the song, one id per line in ascending order, including bard
"""
villagers = {}
song_no = 0
n = int(input())
for id in range(n):
    villagers[str(id+1)] = set()
e = int(input())
for _ in range(e):
    evenings = input().split()
    k = evenings[0]
    evenings = evenings[1:]
    if "1" in evenings:
        song_no += 1
        for villager in evenings:
            villagers[villager].add(song_no)
    else:
        for person in evenings:
            for other_person in evenings:
                villagers[person].update(villagers[other_person])
for final in villagers:
    if len(villagers[final]) == len(villagers["1"]): 
        print(final)