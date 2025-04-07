import json

grades_dict = { 'students' : [ 
               {'firstname': 'jack', 'lastname': 'daniels','examgrade1': 78, 'examgrade2':18,'examgrade3':28 },
               {'firstname': 'homer', 'lastname': 'simpson','examgrade1': 99, 'examgrade2':81,'examgrade3':23 },
               {'firstname': 'lisa', 'lastname': 'farnes','examgrade1': 91, 'examgrade2':23,'examgrade3':23 },
               {'firstname': 'georde', 'lastname': 'yale','examgrade1': 35, 'examgrade2':57,'examgrade3':39 },
               {'firstname': 'manny', 'lastname': 'ahaaty','examgrade1': 91, 'examgrade2':12,'examgrade3':74 }
                                ]
                    }
output_file = open('files/json/json files/students.json','w')
json.dump(grades_dict,output_file)
