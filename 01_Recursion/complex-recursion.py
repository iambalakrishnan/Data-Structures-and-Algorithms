def recursion(number):
    if number > 0:
        print("recursion " , number)
        recursion(number - 1)
        recursion(number - 1)


number = 3
recursion(number)