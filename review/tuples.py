lst = [(num, num**3) for num in range(1,6)]
print(lst)
lst = [num*3 for num in range(1,10)]
print(lst)
lst = [1,2,3,4,5,6,7,8,9]
lst2 = [x**2 for x in lst if x%2 != 0]
print(lst2)
lst = [[77,68,86,73],[96,87,89,81],[70,90,86,81]]
sum = 0
items = 0
for x in lst:
    for y in x:
        sum += y
        items += 1
print(sum/items)