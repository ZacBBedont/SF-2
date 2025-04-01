import json
exam1_average = 0
exam2_average = 0
exam3_average = 0
def spacing(element1,element2):
    return len(element2) - len(element1)
input_file = open('files/json/json files/students.json','r')
input_data = json.load(input_file)
print('firstName','lastName','exam1','exam2','exam3','average')
print('--------------------------------------------')

for student in input_data['students']:
    average = (student['examgrade1']+student['examgrade2']+student['examgrade3'])/3
    exam1_average += student['examgrade1']
    exam2_average += student['examgrade2']
    exam3_average += student['examgrade3']
    print(student['firstname'] + spacing(student['firstname'],'firstName')* " ", 
          student['lastname'] + spacing(student['lastname'],'lastName')* " ",
          str(student['examgrade1'])+ spacing(str(student['examgrade1']),'exam1') * " ",
          str(student['examgrade2'])+ spacing(str(student['examgrade2']),'exam2') * " ",
          str(student['examgrade3'])+ spacing(str(student['examgrade3']),'exam3')* " ",
          str(round(average,2))+ spacing(str(round(average,2)),'average') * " ")
    print('--------------------------------------------')
print('exam1:average ','exam2:average', 'exam3:average')
print('--------------------------------------------')
print(str(round(exam1_average/5,2)) + spacing(str(round(exam1_average/5,2)),'exam1 average')* " ", 
      str(round(exam2_average/5,2)) + spacing(str(round(exam2_average/5,2)),'exam2 average')* " ",
      str(round(exam3_average/5,2)) + spacing(str(round(exam3_average/5,2)),'exam3 average') * " ")
print('--------------------------------------------')