village_no = int(input("how many villages: "))
villages = []
all_neighborhoods = []

for _ in range(village_no):
    villages.append(int(input("village placement: ")))

villages.sort()

for places in range(1,village_no-1):
    neighborhood = (villages[places]+villages[places+1])/2-(villages[places]+villages[places-1])/2
    all_neighborhoods.append(neighborhood)

print(min(all_neighborhoods))
