# Question 1
'''
From your accounts.txt file (from last class) read each line and create 
a dictionary of dictionaries.  The outer dictionary key is the account 
number.  The inner dictionary key is the last name and the value in 
the inner dictionary is the balance.  Print the final dictionary.  
'''
output_file = open('files/txt files/accounts.txt','r')
d = {}
for line in output_file:
    account,name,balance = line.split()
    d[account] = {name : balance}
#print(d)

# Question 2
'''
(a) Open a file called grades.txt for writing that will hold student 
    grade information.  This information will be read from the user.  
    Each input line given by the user is of the form: 
    firstname, lastname, exam1grade, exam2grade, exam3grade.  
    Read grade information for 10 students and write that information 
    to your grades.txt file.  Make sure to close the file after 
    writing to it.  

(b) Once your grades.txt file is populated, read and store the infomration
    from the file.  Determine what data structure (e.g. lists, dictionaries, 
    sets, etc.) would best suit for storing the data in the file.  Once 
    your data is stored, compute the following: 
    (i) the minimum, maximum and average of exam1grade, exam2grade, exame3grade
        for each student and print this information
    (ii) the minimum, maximum and average of exam1grade across all students.
         Do this for exam2grade and exam3grade as well.  
    (iii) the average of the average of all 3 exams for all students.  
'''
def creatGrades():
    output_file = open('files/txt files/grades.txt','w')
    for _ in range(10):
        output_file.write(input() + '\n')
    output_file.close()
def b():
    grades = {}
    exam1_avg = 0
    exam2_avg = 0
    exam3_avg = 0
    input_file = open('files/txt files/grades.txt','r')
    for line in input_file:
        line = line.split()
        grades[(line[0],line[1])] = [line[2],line[3],line[4]]
    for student,grade in grades.items():
        grade = list(map(int,grade))
        print(student, "average is: ", round(sum(grade)/3,2))
        exam1_avg += grade[0]
        exam2_avg += grade[1]
        exam3_avg += grade[2]
    print("exam1 average is",exam1_avg/10)
    print("exam2 average is",exam2_avg/10)
    print("exam3 average is",exam3_avg/10)
    print('the overall average is', (exam1_avg + exam2_avg + exam3_avg)/10/3)

# Question 3
'''
Download into your folder the words.txt file on Lea.  You will notice that each
word in the words.txt file is on a new line.  
(a) Open a new file called words_updated.txt with writing mode, and write all the
    words from the words.txt file continuously one after the other only separated
    by a space.  Make sure that you strip all the white space after each word
    that you read from the words.txt file.  Once you are done, make sure you
    close all files that you had opened.  

(b) Create an integer num_words that will hold the number of words that you have
    in your words_updated.txt (or words.txt) file.  Now prompt the user to read
    an integer k (between 1 and 80) from the user.  Make sure to do input 
    validation so to be assured that the user abides the constraints on k.  

    Open a new file called result.txt with writing mode, and read the words 
    from your words_updated.txt file and write them in result.txt such that
    the number of characters on each line of result.txt is at most k (not
    counting the spaces between the words).  That is, if the next word 
    begin considered fits on the current line, add it to the current line
    (make sure to include a space between each pair of words on the line). 
    Otherwise, put this word on a new line (which will become the new
    current line).

    One you finish writing to your result.txt file, print the content of
    your file.  Make sure to close all files that you have opened.  
'''
words_updated = open('files/txt files/words_updated.txt','w')
words = open('files/words.txt','r')
lst = list(map(str.rstrip,words.readlines()))
for word in lst:
    words_updated.write(word + " ")
num_words = len(lst)
words.close()
words_updated.close()

k = int(input())
words_updated = open('files/txt files/words_updated.txt','r')
result = open('files/txt files/result.txt','w')
line_len = 0
lst = words_updated.readline().split()
for word in lst:
    if (len(word) + line_len) > k:
        line_len = len(word)
        result.write('\n' + word + " ")
    else:
        line_len += len(word)
        result.write(word + " ")
words_updated.close()   
result.close()