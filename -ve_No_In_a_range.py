def pos_No(x,y):
    print("All the negative no present in the range are : ")
    for i in range(x,y+1):
        if i<0:
            print(i)
x=int(input("Enter the start range : "))
y=int(input("Enter the stop range : "))
pos_No(x,y)