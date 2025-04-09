'''
Zaccaria Broomhall Bedont 
Student Id: 2438041
'''


def toCelcius(temp):
    celcius = round((temp - 32)*(5/9),2)
    return celcius

def belowFreezing(temp_dict):
    month_pos = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    cold_months = set()
    months = []
    for month_lst in temp_dict.values():
        for temp_pos in range(len(month_lst)):
            if month_lst[temp_pos] < 0:
                cold_months.add(temp_pos)
    cold_months = list(cold_months)
    for month in cold_months:
        months.append(month_pos[month+1])
    return months

input_file = open('Assignment3/data.txt','r')
temp_dict = {}

for line in input_file:
    line = line.split()
    if len(line) > 0 and line[0].isdigit():
        temp_floats = list(map(float,line[1:]))
        temp_dict[int(line[0])] = list(map(toCelcius,temp_floats))
input_file.close()

output_file = open('Assignment3/data_celcius.txt','w')
init_lines = ['Average monthly temperatures in Dubuque, Iowa, \n','January 1964 through December 1975, n=144\n\n','	JAN	FEB	MAR	APR	MAY	JUN	JUL	AUG	SEP	OCT	NOV	DEC\n']

output_file.writelines(init_lines)
for year in temp_dict:
    output_line = str(year) + ' '*(8-len(str(year)))
    for temp_pos in range(len(temp_dict[year])):
        if temp_dict[year][temp_pos] != temp_dict[year][-1]:
            output_line += str(temp_dict[year][temp_pos]) + ' '*(8-len(str(temp_dict[year][temp_pos])))
        else:
            output_line += str(temp_dict[year][temp_pos])
    if year != 1975:
        output_line = output_line + '\n'
    output_file.writelines(output_line)

output_file.close()
