import json

#convert from JSON to python

student_record = '{"name":"Lucy","year":"1","college":"Dawson"}'
parsed_record = json.loads(student_record)

student_record = {'name':'Lucy','year':1,'college':'Dawson'}
student_record_json = json.dumps(student_record)

print(parsed_record)
print(student_record_json + '\n\n\n\n\n')

print(json.dumps({'name':'lucy','year':1}))
print(json.dumps(['red','green','blue',1]))
print(json.dumps(('red','green',[1,2,3,'apple'],1)))
print(json.dumps('hello world'))
print(json.dumps(12))
print(json.dumps(12.33))
print(json.dumps([True,False,None]))