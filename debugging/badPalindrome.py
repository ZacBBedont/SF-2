def isPalindrome(lst):
    """
    Determine if lst is a palindrome
    :param lst: lst is a list
    :return: True if lst is a palindrome, otherwise false
    """
    temp = lst[:]
    temp.reverse()
    return temp == lst

def silly(n):
    """
    get n inputs from user. Print "yes" if the sequence of inputs forms a palindrome; "no" otherwise
    :param n: n is an integer > 0
    :return: None
    """
    result = []
    for i in range(n):
        elem = input("enter element: ")
        result.append(elem)
    if isPalindrome(result):
        print("Yes")
    else:
        print("No")

silly(2)
