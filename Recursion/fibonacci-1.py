"""Finding the nth Fibonacci number"""


def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))



num = int(input("Enter a number: "))  
if num <= 0:  
    print("please enter value more than 2")
else:   
    for i in range(num):  
        last_value = fib(i)
    print(last_value)