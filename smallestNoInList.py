def smallList(n):
    x=n[0]
    for i in n:
        if i<x:
            x=i
    print("The smallest value in the list is ",x)

n=[11,22,3,64,55]
smallList(n)