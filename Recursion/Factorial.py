def myfact(n):
    if n == 1:
        return n
    else:
        return n * myfact(n-1)


number = 5

if number < 0:
    print("Factorial does not exist for negative numbers")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    print(f"Factorial of {number} is {myfact(number)}")