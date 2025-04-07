"""
Zaccaria Broomhall Bedont
Student Id:2438041
"""

def toCelcius(temp):
    celcius = round((temp - 32)*(5/9),2)
    return celcius

def avgTempYear(temp_dict,year):
    try:
        values = temp_dict[year]
        average =  sum(values)/len(values)
    except KeyError:
        print("sorry! That is not a year in our data.")
    else:
        return round(average,2)

def topThreeYears(temp_dict):
    avg_set = set()
    top_three = []
    for year in temp_dict:
        average = avgTempYear(temp_dict,year)
        avg_set.add(average)
    for _ in range(3):
        top_three.append(max(avg_set))
        avg_set.remove(max(avg_set))
    return top_three

def avgTempMonth(temp_dict,month):
    month_pos = {'JAN':1,'FEB':2,'MAR':3,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12}
    month_lst = []
    for value in temp_dict.values():
        month_lst.append(value[month_pos[month]-1])
    month_avg = sum(month_lst)/len(month_lst)
    return round(month_avg,2)

input_file = open('Assignment3/data.txt','r')
temp_dict = {}

for line in input_file:
    line = line.split()
    if len(line) > 0 and line[0].isdigit():
        temp_floats = list(map(float,line[1:]))
        temp_dict[int(line[0])] = list(map(toCelcius,temp_floats))