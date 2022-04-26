def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))


# while True:
#     try:
#         n = int(input("Enter a number: "))
#         if n <= 0:
#             print("Please enter a positive number")
#             continue
#         else:
#             for i in range(n):
#                 print(fib(i))
#         break
#     except ValueError:
#         print("Please enter a valid integer")
#         continue


num = int(input("Enter a number: "))  
if num <= 0:  
    print("please enter value more than 2")
else:   
    for i in range(num):  
        print(fib(i))