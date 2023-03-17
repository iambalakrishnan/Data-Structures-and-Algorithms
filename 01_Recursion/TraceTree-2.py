def TraceTreeTwo(number):
    if number > 0:
        TraceTreeTwo(number - 1)
        print("TraceTree TWO " , number)


number = 5
TraceTreeTwo(number)