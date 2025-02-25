#given a list of lists, remove the empty list from it by keeping the originial list as is
lst = [[1,2],[],[3,4],[],[5]]

lst2 = []

for element in lst:
    if element:
        lst2.append(element)
print(lst2)


#write the same thing using only list comprehension
lst2 = [element for element in lst if element]
print(lst2)

#remove the empty lists by modifying the original list of lists

lst = [element for element in lst if element]
print(lst)




lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lst2 = [num**2 for num in lst if num>3 and num<11]
print(lst2)

lst = [23,35,65,73,83,24]
num = [25,65,24,34,34,543]
lst2 = [x + 5 for x in lst if x in num]
print(lst2)








lst_2d = [["4","3","15"],["92","1"],["0","011011","76","8"]]
result = []


result = [[int(i) for i in row] for row in lst_2d]
print(result)




lst = [[1,23,45,44],[2,2,5],[90,1110111,72,8,5],[0],[-18,9,0]]
mode = True

def sort(type,mini_lst):
    for y in range(len(mini_lst)):
        for x in range(len(mini_lst)):
            if mini_lst[x] > mini_lst[y]:
                mini_lst[x],mini_lst[y] = mini_lst[y],mini_lst[x]
    if type:
        mini_lst = mini_lst[::-1]
    return mini_lst
for element in range(len(lst)):
    lst[element] = sort(mode,lst[element])
print(lst)


mtrx = [[1,2],[3,4],[5,6]]

lst = [3,726272727,23,2]

current_max = lst[0]
for i in range(1,len(lst)):
    if lst[i] > current_max:
        current_max = lst[i]
print(current_max)

from math import factorial

def binom(n,k):
    return factorial(n)//(factorial(n-k)*factorial(k))
l = binom(3,2)
print(l)

def pascals(rows): #space and time complexity, n^3 and n^2, more efficitent by defining edge cases and adding the oher ones by indexing
    triangle = []
    for row in range(rows):
        individual = []
        for upwards in range(row+1):
            individual.append(binom(row,upwards))
        print(*individual)
pascals(4)