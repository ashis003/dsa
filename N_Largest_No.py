def N_Largest_No(n,x):
    print("The list before sorting : ",n)
    n.sort()
    print("The list after sorting : ",n)
    print("The required no at that position : ",n[-x])
n=[10,12,8,11,13]
x=int(input("Enter the position to get the largest no : "))
N_Largest_No(n,x)
