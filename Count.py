def count(n,x):
    count=0
    for i in n:
        if i==x:
            count=count+1
    print('The occurance of the no {} in the list is {} '.format(x, count))
n=[1,2,3,4,5,1,6,8,1,9]
x=int(input("Enter the no to check the no of occurance in the list : "))
count(n,x)

