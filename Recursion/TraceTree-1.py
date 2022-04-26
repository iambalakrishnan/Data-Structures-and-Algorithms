def TraceTree(number):
    if number > 0:
        print("TraceTree " , number)
        TraceTree(number - 1)


number = 5
TraceTree(number)