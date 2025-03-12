'''
write a function called combine2 that takes 2 dictionaires d1 and d2
    and combines them together into a new dictionary and returns
    this dictionary.
Here are the details: 
--> d1 and d2 are dictionary of dictionaries.  The inner dictionary
    values are lists of integers
--> if d1 and d2 have the same key, for which the respective inner
    dictionaries both in d1 and d2 also have the same key k, then
    k is added as a key to the  combined dictionary and the value
    is the sum of the values in the respective lists.  

>>> d1 = {'a': {3: [2], 4: [5, 6]}}
>>> d2 = {'a': {3: [8, 12]}}
>>> combine2(d1, d2)
{3: 22}
'''
def combine(d1,d2):
    newd = {}
    for dictionary in d1:
        if dictionary in d2:
            for key in d1[dictionary]:
                if key in d2[dictionary]:
                    newd[key] = sum(d1[dictionary][key])+sum(d2[dictionary][key])
    return newd
#print(combine({'a': {3: [2], 4: [5, 6]}},{'a': {3: [8, 12]}}))


'''
create a file birthdays.py that will do the following:

(a) write a function that reads birthdays of people
    from the user and stores them in a dictionary
    of dictionaries.  Once the user enters 'stop', you 
    will read no more input from the user.  You may
    assume the user will give valid input.

    Sample Input:
    month day name: February 23 Bob
    month day name: May 3 Katie
    month day name: May 8 Paul
    month day name: May 8 Lucy
    month day name: stop

    Sample Ouput (i.e. returned by function)
    { 'February': {'23': ['Bob']},
    'May': {'3': ['Katie'], '8': ['Paul', 'Lucy']} }
'''

def birthday_dict():
    birthdays = {}
    while True:
        birthday = input("month day name: ")
        if birthday == "stop":
            return birthdays
        month,day,name = birthday.split()
        birthdays[month] = birthdays.get(month,{day:[name]})
        birthdays[month][day] = birthdays[month].get(day,[name])
        for key in birthdays[month]:
            if key == day and name not in birthdays[month][key]:
                birthdays[month][key].append(name)
#print(birthday_dict())
        
    

'''
(b) Write a function called mostCovered that will take 
the dictionary entered by the user in part (a) and
return the month that has the most number of 
birthdays
'''
def mostCovered(d1):
    most = 0
    best_month = []
    for month in d1:
        count = 0
        for name in d1[month].values():
            count += len(name)
        if count > most:
            most = count
            best_month = [month]
        elif count == most:
            best_month.append(month)
    return best_month
#print(mostCovered(birthday_dict()))
'''
(c) write a function called invert() that will take
the birthday month dictionary entered by the user in
part(a) and return the equivalent brithday dictionary

Sample Input is the dictionary returned in part (a)

Sample Output:
{'Bob': ('February', '23'), 
'Katie': ('May', '3'),
'Paul': ('May', '8'), 
'Lucy': ('May', '8')}
'''

def invert(d1):
    newd = {}
    for month in d1:
        for day in d1[month]:
            for name in d1[month][day]:
                newd[name] = (month,day)
    return newd

print(invert(birthday_dict()))