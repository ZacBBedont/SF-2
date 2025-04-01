'''
print story only to the user
count the number of words in the story
'''
book_txt = open('files/txt files/ugly_duckling.txt','r')
book_lst = book_txt.readlines()
first = True
words_len = 0
words_dict = {}
words_lst = []
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
    print(line)
    words_len += len(line.rstrip().split())
    words = line.rstrip().split()
    for word in words:
        words_dict[word] = words_dict.get(word,0)
        words_dict[word] += 1
for word in words_dict:
    words_lst.append((word,words_dict[word]))
for pos in range(len(words_lst)):
    for pos2 in range(len(words_lst)):
        if words_lst[pos][1] < words_lst[pos2][1]:
            words_lst[pos],words_lst[pos2] = words_lst[pos2],words_lst[pos]

print(words_len)
print(words_lst)