'''
Question1:

Given a dictionary of keys that are strings and/or integers, 
values are lists, write a snippet of code that returns the total number
of elements of all lists that have keys as strings.  
'''
def stringKeys(dict):
    count = 0
    for key in dict.keys():
        if type(key) == str:
            count += len(dict[key])
    return count
dict = {1:["hello"],2:["goodbye"],3:["that", "was", "rude"],4:["I", "don't", "care"], "well I do": [5,6], "no one loves you":[6]}
#print(stringKeys(dict))


'''
Question2:

Write a function wordTally that takes an integer argument 
n and reads n words from the user.  Note that the user
may enter the same word multiple times.  
Your function should tally up how many times each word
occurs that the user has entered and store it in a dictionary
where the keys are the words and the values are the number
of times each word occurs.  
Return this dictionary. 

You may only create one collection: one dictionary
'''
def wordTally(n):
    wordCount = {}
    for _ in range(n):
        word = input()
        wordCount[word] = wordCount.get(word,0) + 1
    return wordCount
#print(wordTally(3))


'''
Quesiton3: 

write a function called invertDictionary that takes a 
dictionary d as an argument.  This function inverts the
provided dictionary.  That is, the keys become the values
(as lists) and the values become the keys. 

Note that d may have repetitive values, in which case in 
the inverted dictionary only one of these values
will be used as a key. For such a key, in the inverted
dictionary the value is a list of all such possible
keys from d

For example: 
d = {3: 5, 4: 5, 6: 1}
d_inverted = {5: [3, 4], 1: [6]}
'''
def invertDictionary(d):
    newd = {}
    for key,element in d.items():
        newd[element] = newd.get(element,[])
        newd[element].append(key)
    return newd
d = {3: 5, 4: 5, 6: 1}
#print(invertDictionary(d))

'''
Question 4:

Given a sequence of m words and an integer k, find the
k-th most common words.  A word w is the k-th most 
common if exactly k-1 distinct words occur more
frequently than w. 
'''
def kthMostCommon(m,k):
    d = wordTally(m)
    d = invertDictionary(d)
    answer = []
    for key in d:
        less_word_count = 0
        for second_key in d:
            if key < second_key:
                less_word_count += len(d[second_key])
        if less_word_count == k-1:
            answer = d[key]
    return answer
m = 14
k = 5
print(kthMostCommon(m,k))
