"""Finding the sum of  Fibonacci series"""


def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))



num = int(input("Enter a number: "))  
if num <= 0:  
    print("please enter value more than 2")
else:
    sum = 0   
    for i in range(num):  
        sum = sum + fib(i)
    print(sum)