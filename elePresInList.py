def presList(n,x):
    for i in n:
        if i==x:
            print("Present")
            break
    else:
        print("Absent")
n=[1,22,3,4,5]
x=int(input("Enter to value check with : "))
presList(n,x)
