'''
print story only to the user
count the number of words in the story
'''
book_txt = open('files/txt filesbook.txt','r')
book_lst = book_txt.readlines()
first = True
line_len = 0
for line in range(len(book_lst)):
    try:
        book_lst[line+1]
    except:
        book_lst = book_lst[:index]
        break
    if book_lst[line] == '\n' and first == True:
        book_lst = book_lst[line:]
        first = False
    elif book_lst[line] == '\n':
        index = line
for line in book_lst:
    line_len += len(line.rstrip().split())
print(line_len)
    