import time
def search(collection,value):
    """
    search for value in the collection
    """
    for i in collection:
        found = value in collection
    return found
#s1.update(s2)
#=s1 U s2

lst = list(range(1,50000))
s = set(range(1,50000))
start = time.time()
print(search(lst,50000))
end = time.time()
print(f"algorithm list: {end-start}")
start = time.time()
print(search(s,50000))
end = time.time()
print(f"algorithm list: {end-start}")