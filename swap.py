def swap(x,a,b):
    temp = x[a]
    x[a] = x[b]
    x[b] = temp
    print(x)
x=[1,2,3,4,5]
a=int(input("Enter the position of the first no to change with : "))
b=int(input("Enter the position of the second no to change with : "))
swap(x,a,b)
