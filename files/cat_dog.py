try:
    cats_txt = open('files/txt files/cats.txt','r')
    dogs_txt = open('files/txt files/dogs.txt','r')
except FileNotFoundError:
    pass
else:
    for line in cats_txt:
        print(line.rstrip())
    for line in dogs_txt:
        print(line.rstrip())