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


input_string = input("Enter a string: ")
string = reverse(input_string)
print(string)

str = reverseTwo(input_string) 
print(str)