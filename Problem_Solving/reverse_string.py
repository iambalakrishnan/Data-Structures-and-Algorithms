#Define string reverse function
def reverse(string):
    string = string[::-1]
    return string

#Approach 2
def reverseTwo(string):
    str = ""
    for i in string:
        str = i + str
    return str