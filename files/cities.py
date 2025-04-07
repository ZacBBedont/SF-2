cities_txt = open('files/txt files/cities.txt','w')
n_list = []
for _ in range(5):
    n = int(input())
    n_list.append(n)
    for _ in range(n):
        city,state = input().split()
        cities_txt.write(city+ " " + state+'\n')
    cities_txt.write('\n')
cities_txt.close()
cities_txt = open('files/txt files/cities.txt','r')
for input_id in range(5):
    d = {}
    for _ in range(n_list[input_id]):
        city,state = cities_txt.readline().split()
        d[(city[0:2],state)] = d.get((city[0:2],state),0)
        d[(city[0:2],state)] += 1
    cities_txt.readline()
    pairs = 0
    for key1,key2 in d:
        if (key2,key1) in d and key2 != key1:
            pairs += d[(key2,key1)] * d[(key1,key2)]
            if d[(key1,key2)] < 0:
                d[(key1,key2)] = 0
    print(int(pairs/2))