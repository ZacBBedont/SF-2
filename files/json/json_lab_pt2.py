import json

def spacing(element1,element2):
    return len(element2) - len(element1)
input_file = open('files/json/json files/students.json','r')
input_data = json.load(input_file)
print('firstName','lastName','exam1','exam2','exam3','average')
print('--------------------------------------------')

for student in input_data['students']:
    average = (student['examgrade1']+student['examgrade2']+student['examgrade3'])/3
    print(student['firstname'] + spacing(student['firstname'],'firstName')* " ", 
          student['lastname'] + spacing(student['lastname'],'lastName')* " ",
          str(student['examgrade1'])+ spacing(str(student['examgrade1']),'exam1') * " ",
          str(student['examgrade2'])+ spacing(str(student['examgrade2']),'exam2') * " ",
          str(student['examgrade3'])+ spacing(str(student['examgrade3']),'exam3')* " ",
          str(round(average,2))+ spacing(str(round(average,2)),'average') * " ")
    print('--------------------------------------------')
