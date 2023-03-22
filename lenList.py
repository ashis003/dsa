def userList(n):
    list=[]
    print("Enter the no to enter in the list : ")
    for i in range(0,n):
        ele = int(input())
        list.append(ele)
    print("The element in the list are : ",list)
    print("The length of the list is : ",len(list))
    #counting len without built-in function
    count=0
    for j in list:
        count=count+1
    print("Counting len without built-in function",count)


n=int(input("Enter the size of the list : "))
userList(n)









