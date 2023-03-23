def largestNoInList(n):
    n.sort()
    print("The smallest number in the list is : ",n[0])
    print("The largest number in the list is : ",n[-1])
    print("The smallest number in the list is : ",min(n))
    print("The largest number in the list is : ",max(n))
n=[1,42,33,34,35]
largestNoInList(n)