file_name = 'files/txt files/book.txt'
try:
    input_file = open(file_name,'r')
except FileNotFoundError:
    print('file does not exist')
    output_file = open(file_name,'w')
else:
    for line in input_file:
        print(line.rstrip())
input_file = open('files/txt files/blah.txt','r')
blah_lst = input_file.readlines()
output_file.writelines(blah_lst)
output_file.close()
input_file.close()