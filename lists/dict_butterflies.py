def new_sighting(butterflies,sighting):
    butterflies[sighting] = butterflies.get(sighting,0) + 1

butterflies = {"Monarch":5,"Painted Lady":2,"Bronze Copper":12,"orange Sulfur":7}

for kind,count in butterflies.items():
    print(kind ,":",count)