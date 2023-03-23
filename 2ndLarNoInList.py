def secondLargestNo(n):
    n.sort()
    print("The smallest no in the list is : ",min(n))
    print("The largest no in the list is : ", max(n))
    print("The 2nd largest element in the list is : ",n[-2])
n=[1,22,1,3,21,4,9]
secondLargestNo(n)


