import json

student_json = open('files/json/json files/student.json','r')
student_data = json.load(student_json)
print(type(student_data),student_data)
student_json.close()

#student_json = open('files/json/json files/student.json','r')
#for line in student_json:
#print(line)
#print(type(line))
#student_json.close()

output_file = open('files/json/json files/butterflies.json','w')
d = {'painted lady':1,'bronze copper':12,'monarch':5}
json.dump(d,output_file)
output_file.close()